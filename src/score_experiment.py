"""
This is a runner script to score and analyze an exam experiment. It is designed to be run from the command line like this:
$ poetry run python3 src/score_experiment.py \
    --exam-type mbe \
    --exam-id ncbe-pdf-001 \
    --experiment-id 001

It will produces the following files under results/:
    * results/{exam_type}/{exam_id}/{experiment_id}/all_results.csv: a CSV file with all every question from every
        session graded
"""

# imports
import argparse
import datetime
import json
from pathlib import Path

# packages
import pandas
import tqdm

# project imports
from exams.experiment_data import get_experiment_session_list
from exams.choice_exam import parse_choice_response

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam-type", type=str, required=True)
    parser.add_argument("--exam-id", type=str, required=True)
    parser.add_argument("--experiment-id", type=int, default=1)
    parser.add_argument("--num-samples", type=int, default=3)

    args = parser.parse_args()

    # set the experiment id
    experiment_id = args.experiment_id

    # set the exam id
    exam_id = args.exam_id.lower()

    # set the exam type
    exam_type = args.exam_type.lower()

    # set the number of samples
    num_samples = args.num_samples

    # get the list of sessions
    session_list = get_experiment_session_list(exam_type, exam_id, experiment_id)

    # iterate through all sessions
    all_results = []
    for session_path in tqdm.tqdm(session_list):
        # load the session data
        session_data_file = session_path / "session.json"
        session_data = json.loads(session_data_file.read_text())

        # get the session id from the last file directory path
        session_id = session_path.parts[-1]

        # get parameters from the session data
        session_parameters = session_data["parameters"]
        try:
            session_duration = (
                    datetime.datetime.fromisoformat(session_data["session_end"])
                    - datetime.datetime.fromisoformat(session_data["session_start"])
            ).total_seconds()
        except Exception as e:
            session_duration = None

        # parse each question response and add to the results
        for question in session_data["question_data"]:
            # check if we have at least one model_response string
            if len(question["model_response"]) == 0:
                continue

            # parse the response
            question_answer_data = parse_choice_response(question["model_response"][0])

            question_record = {
                "exam_type": exam_type,
                "exam_id": exam_id,
                "experiment_id": experiment_id,
                "session_id": session_id,
                "model": session_data["engine"],
                "prompt": session_data["prompt_method"],
                "question_number": question["question_number"],
                "question_category": question["question_category"],
                # answers
                "answer": question_answer_data["answer"],
                "second_answer": question_answer_data["second_answer"],
                "third_answer": question_answer_data["third_answer"],
                "correct_answer": question["correct_answer"],
                # correctness of answers
                "is_correct": (
                        question_answer_data["answer"].upper() == question["correct_answer"].upper()
                        if question_answer_data["answer"] is not None else False
                ),
                "is_second_correct": (
                        question_answer_data["second_answer"].upper() == question["correct_answer"].upper()
                        if question_answer_data["second_answer"] is not None else False
                ),
                "is_third_correct": (
                        question_answer_data["third_answer"].upper() == question["correct_answer"].upper()
                        if question_answer_data["third_answer"] is not None else False
                ),
            }

            # add top two and three
            question_record["is_top_two_corrrect"] = (
                    question_record["is_correct"] or question_record["is_second_correct"]
            )
            question_record["is_top_three_corrrect"] = (
                    question_record["is_correct"]
                    or question_record["is_second_correct"]
                    or question_record["is_third_correct"]
            )

            # add the session parameters
            question_record.update(session_parameters)

            # add the session duration
            question_record["session_duration"] = session_duration

            # add the question record to the results
            all_results.append(question_record)


    # get as dataframe and store to CSV in that path
    all_results_df = pandas.DataFrame(all_results)

    # create the results directory relative to the last session path
    # get results path from exam_type, exam_id, experiment_id path components
    result_output_path =  Path(__file__).parent.parent / "results" / exam_type / exam_id / f"experiment-{experiment_id:03d}" / "all_results.csv"

    # write the CSV
    all_results_df.to_csv(result_output_path, index=False, encoding="utf-8")

    # get the per-session results for aggregation
    session_result_df = all_results_df.groupby(["model", "prompt", "temperature", "session_id"]).agg(
        {
            # averages
            "is_correct": "mean",
            "is_top_two_corrrect": "mean",
            "is_top_three_corrrect": "mean",
            "session_duration": "mean",
            "session_id": "count",
        }
    )

    # aggregate the results to model/prompt/temperature
    summary_result_df = session_result_df.groupby(["model", "prompt", "temperature"]).agg(
        is_correct=('is_correct', 'mean'),
        is_top_two_corrrect=('is_top_two_corrrect', 'mean'),
        is_top_three_corrrect=('is_top_three_corrrect', 'mean'),
        session_duration=('session_duration', 'mean'),
        correct_std=('is_correct', 'std'),
        session_id=('session_id', 'count'),
    )

    # add column labels
    summary_result_df.columns = [
        "Mean Accuracy",
        "Mean Top Two Accuracy",
        "Mean Top Three Accuracy",
        "Mean Session Duration",
        "Std. Dev. Accuracy",
        "Session Count",
    ]

    print(summary_result_df.to_csv())


if __name__ == "__main__":
    main()