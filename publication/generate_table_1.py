# imports
import textwrap
from pathlib import Path

# packages
import numpy
import matplotlib.pyplot
import pandas
import seaborn


if __name__ == "__main__":
    # load data
    exam_id = "ncbe-pdf-002"
    experiment_id = "experiment-001"
    result_path = Path(__file__).parent.parent / "results"
    df = pandas.read_csv(result_path / "mbe/" / exam_id / experiment_id / "all_results.csv")

    df.columns = [
        "Exam Type",
        "Exam ID",
        "Experiment ID",
        "Session ID",
        "Model",
        "Prompt",
        "Question Number",
        "Question Category",
        "Answer",
        "Second Answer",
        "Third Answer",
        "Correct Answer",
        "Correct",
        "Second Correct",
        "Third Correct",
        "Top Two Correct",
        "Top Three Correct",
        "Temperature",
        "Best Of",
        "Max Tokens",
        "Session Duration",
    ]

    model_filter_list = [
        'openai:hidden-gpt-4-model-name',
        'openai:chat-davinci-003-alpha',
        'openai:text-davinci-003',
    ]

    NCBE_CATEGORY_CORRECT_RATES = {
        "Civil Procedure": 0.59,
        "Constitutional Law": 0.72,
        "Contracts": 0.70,
        "Criminal Law and Procedure": 0.71,
        "Evidence": 0.65,
        "Real Property": 0.65,
        "Torts": 0.71
    }

    category_list = ['Civil Procedure', 'Constitutional Law', 'Contracts',
       'Criminal Law and Procedure', 'Evidence', 'Real Property', 'Torts']

    # Show Top Two Correct Rate by Model and Category but only two digits of precision
    table_df = df.loc[df["Model"].isin(model_filter_list)].groupby(["Question Category", "Model"])["Correct"].mean().unstack()

    # change the table column order to match the list
    table_df = table_df[model_filter_list]

    # combine with the NCBE category correct rates
    ncbe_df = pandas.DataFrame.from_dict(NCBE_CATEGORY_CORRECT_RATES, orient="index", columns=["NCBE"])
    table_df = table_df.join(ncbe_df)

    # relabel all the models
    table_df = table_df.rename({
        'openai:hidden-gpt-4-model-name': 'GPT-4',
        'openai:chat-davinci-003-alpha': 'ChatGPT',
        'openai:text-davinci-003': 'GPT-3.5',
    }, axis='columns')

    # reorder so we have GPT-3.5, ChatGPT, GPT-4, and NCBE
    table_df = table_df[['GPT-3.5', 'ChatGPT', 'GPT-4', 'NCBE']]

    print((table_df * 100.0).round(2).to_latex(float_format="%.1f%%"))
