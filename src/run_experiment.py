"""
This is a runner script to execute an exam experiment. It is designed to be run from the command line like this:
$ poetry run python3 src/run_experiment.py \
    --exam-type mbe \
    --exam-version ncbe-pdf-001 \
    --experiment-id 001 \
    --num-samples 3

We test the following models:
 * text-ada-001
 * text-babbage-001
 * text-curie-001
 * text-davinci-001
 * text-davinci-003
 * ...

We test the following parameters:
 * temperature in [0.0, 0.5, 1.0]
 * best_of in [1, 2]
"""

# imports
import argparse

# packages
import tqdm

# project imports
import engines.engine_openai
from exams.choice_exam import run_choice_exam
from exams.choice_prompts import MBE_PROMPT_LIST, MPRE_PROMPT_LIST
from exams.essay_exam import run_essay_exam
from exams.essay_prompts import MEE_PROMPT_LIST, MEE_CHAT_PROMPT_LIST

engines.engine_openai.OPENAI_VALID_PARAMETERS = {
    "temperature": [0.0, 0.5, 1.0],
    "best_of": [1,],
    "max_tokens": [2048],
}

MODEL_SET = [
    "text-ada-001",
    "text-babbage-001",
    "text-curie-001",
    "text-davinci-001",
    "text-davinci-002",
    "text-davinci-003",
    # "chat-davinci-003-alpha",
    # "hidden-gpt-4-model-name"
]


def main():
    """Main method to run the exam across all parameters."""
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

    # set the prompt list
    if exam_type == "mbe":
        prompt_list = MBE_PROMPT_LIST
        exam_method = run_choice_exam
    elif exam_type == "mpre":
        prompt_list = MPRE_PROMPT_LIST
        exam_method = run_choice_exam
    elif exam_type == "mee":
        prompt_list = MEE_PROMPT_LIST
        exam_method = run_essay_exam
    else:
        raise ValueError(f"Invalid exam type: {exam_type}")

    # iterate over all models
    model_prog_bar = tqdm.tqdm(MODEL_SET)
    for model_name in model_prog_bar:
        # set the engine
        engine = engines.engine_openai.OpenAIEngine(model=model_name)

        # iterate over all engine parameters
        for parameter_set in engine.get_valid_parameters():
            # set the engine parameters
            engine.set_parameters(parameter_set)

            # update prog bar
            model_prog_bar.set_description(
                f"Model: {model_name} | Parameters: {parameter_set}"
            )

            # iterate over all prompts
            for prompt_method in prompt_list:
                # run the exam
                exam_method(
                    exam_type=exam_type,
                    exam_id=exam_id,
                    experiment_id=experiment_id,
                    prompt_method=prompt_method,
                    engine=engine,
                    num_samples=num_samples,
                )


if __name__ == "__main__":
    main()
