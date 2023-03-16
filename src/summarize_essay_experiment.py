"""
This is a runner script to summarize the test of essay exam experiments.

It is designed to be run from the command line like this:
$ poetry run python3 src/score_experiment.py \
    --exam-type mee \
    --exam-id ncbe-pdf-001 \
    --experiment-id 001
"""

# imports
import argparse
import datetime
import json
import numpy
from collections import Counter
from pathlib import Path

# packages
import pandas
import spacy
import tqdm

# project imports
from exams.experiment_data import get_experiment_session_list

# we really only need tokenizer and NER
nlp_en = spacy.load("en_core_web_md")


def get_text_features(text: str) -> dict:
    """
    Get text features frmo a response, including:
        - entropy: Shannon entropy of a text string's tokens.
        - num tokens
        - num sentences
        - num proper nouns
    """
    # get the tokens
    tokens = nlp_en(text)

    # get the token frequency and total counts
    token_counts = Counter([token.text for token in tokens])
    num_tokens = sum(token_counts.values())
    num_sentences = len(list(tokens.sents))

    # get the probabilities and entropy
    probabilities = [count / len(tokens) for count in token_counts.values()]
    entropy = -sum([p * numpy.log2(p) for p in probabilities])

    # get the number of proper noun tokens (not same as NPE count post-merge)
    num_proper_nouns = sum([1 for token in tokens if token.pos_ == "PROPN"])

    # check how many tokens are labeled as LAW
    num_ent_law_tokens = sum([1 for token in tokens if token.ent_type_ == "LAW"])

    return {
        "entropy": entropy,
        "num_tokens": num_tokens,
        "num_sentences": num_sentences,
        "num_propn_tokens": num_proper_nouns,
        "num_ent_law_tokens": num_ent_law_tokens,
    }

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam-type", type=str, required=True)
    parser.add_argument("--exam-id", type=str, required=True)
    parser.add_argument("--experiment-id", type=int, default=1)

    args = parser.parse_args()

    # set the experiment id
    experiment_id = args.experiment_id

    # set the exam id
    exam_id = args.exam_id.lower()

    # set the exam type
    exam_type = args.exam_type.lower()


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
            if question["model_response"] and len(question["model_response"]) > 0:
                # only score first response in event we have multiple
                model_response = question["model_response"][0]

                # get the length of the response in chars and tokens
                response_length_char = len(model_response)

                # get the text features
                text_features = get_text_features(model_response)

                # question record
                all_results.append(
                    {
                        "exam_type": session_data["exam_type"],
                        "exam_id": session_data["exam_id"],
                        "experiment_id": session_data["experiment_id"],
                        "prompt_method": session_data["prompt_method"],
                        "engine": session_data["engine"],
                        "temperature": session_parameters["temperature"],
                        "best_of": session_parameters["best_of"],
                        "max_tokens": session_parameters["max_tokens"],
                        "session_id": session_id,
                        "session_duration": session_duration,
                        "question_number": question["question_number"],
                        "question_category": question["question_category"],
                        "length_char": response_length_char,
                        "length_token": text_features["num_tokens"],
                        "length_sentence": text_features["num_sentences"],
                        "entropy": text_features["entropy"],
                        "num_propn_tokens": text_features["num_propn_tokens"],
                        "num_ent_law_tokens": text_features["num_ent_law_tokens"],
                    })

    # create the final df
    df = pandas.DataFrame(all_results)

    # save the results
    output_path = (
            Path(__file__).parent.parent / "results" / exam_type /
            exam_id / f"experiment-{experiment_id:03d}" / "summary.csv"
    )
    df.to_csv(output_path, index=False)

    # output some basic tables
    print("Mean response summarization metrics by engine:")
    print(
        df.groupby("engine")
        [["length_char", "length_token", "length_sentence", "entropy",
          "num_propn_tokens", "num_ent_law_tokens"]]
        .mean()
    )

    print("SEM response summarization metrics by engine:")
    print(
        df.groupby("engine")
        [["length_char", "length_token", "length_sentence", "entropy",
          "num_propn_tokens", "num_ent_law_tokens"]]
        .sem()
    )

    # now do the same thing but by prompt_method instead of engine
    print("Mean response summarization metrics by prompt_method:")
    print(
        df.groupby("prompt_method")
        [["length_char", "length_token", "length_sentence", "entropy",
          "num_propn_tokens", "num_ent_law_tokens"]]
        .mean()
    )

    print("SEM response summarization metrics by prompt_method:")
    print(
        df.groupby("prompt_method")
        [["length_char", "length_token", "length_sentence", "entropy",
          "num_propn_tokens", "num_ent_law_tokens"]]
        .sem()
    )


if __name__ == "__main__":
    main()