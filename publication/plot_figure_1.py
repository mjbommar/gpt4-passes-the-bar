# imports
from pathlib import Path

# packages
import numpy
import matplotlib.pyplot
import pandas


NCBE_CATEGORY_CORRECT_RATES = {
    "Civil Procedure": 0.59,
    "Constitutional Law": 0.72,
    "Contracts": 0.70,
    "Criminal Law and Procedure": 0.71,
    "Evidence": 0.65,
    "Real Property": 0.65,
    "Torts": 0.71
}

# add this path to the matplotlib font manager
# add all fonts under ~/.local/share/fonts/ to the matplotlib font manager
for font_file in Path("~/.local/share/fonts/").rglob("*.ttf"):
    matplotlib.font_manager.fontManager.addfont(font_file)

# set /usr/share/fonts/truetype/noto/NotoSerif-SemiCondensedThin.ttf as default font
matplotlib.font_manager.fontManager.addfont(Path("/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"))
matplotlib.rcParams["font.family"] = "Noto Serif"
matplotlib.rcParams.update({"font.size": 14})


def plot_category_bar_chart(session_df: pandas.DataFrame) -> matplotlib.figure.Figure:
    """Plot the accuracy bar chart with both the NCBE and GPT-3 correct rates by
    Question Category for publication, including the error bars for GPT-3 correct rates
    based on the standard error of the mean.  Make the NCBE bars in a light blue
    and the GPT-3 bars in a light red."""

    # set the font size to 14
    matplotlib.pyplot.rcParams["font.size"] = 12

    # font color to 34343 80%
    matplotlib.pyplot.rcParams["text.color"] = "#343434"

    # set the background color to white
    matplotlib.pyplot.rcParams["figure.facecolor"] = "white"

    # set the axes background color to white
    matplotlib.pyplot.rcParams["axes.facecolor"] = "white"

    # set the axes grid color to white
    matplotlib.pyplot.rcParams["axes.grid"] = False

    # set grid lines to 343434
    matplotlib.pyplot.rcParams["grid.color"] = "#343434"

    category_list = list(reversed(['Civil Procedure', 'Constitutional Law', 'Contracts',
                     'Criminal Law and Procedure', 'Evidence', 'Real Property', 'Torts']))

    # get the NCBE correct rates
    ncbe_correct_rates = [
        NCBE_CATEGORY_CORRECT_RATES[category]
        for category in category_list
    ]

    # only include these models
    model_filter_list = [
        'openai:text-davinci-003',
        'openai:chat-davinci-003-alpha',
        'hidden-gpt-4-model-name' # NOTE: blinded
    ]

    # plot the bars
    fig, ax = matplotlib.pyplot.subplots(figsize=(12, 8))

    # shade the region between 58-62% correct as the passing region
    matplotlib.pyplot.axvspan(0.58, 0.62, color="#343434", alpha=0.1)

    # label the passing region with text
    matplotlib.pyplot.text(0.515, 4.865, "Passing Region", fontsize=14, color="#343434", alpha=1.0)

    # filter to only these model values
    session_df = session_df[session_df["Model"].isin(model_filter_list)]
    category_model_df = session_df.groupby(["Model", "Question Category"])["Correct"].mean()

    # next, plot the values for 'openai:text-davinci-003' side by side
    # with the NCBE values offset by 0.1 to the right
    matplotlib.pyplot.barh(
        numpy.arange(len(category_list)) / 10.0 + 4.0,
        category_model_df.loc['openai:text-davinci-003', category_list],
        #category_model_df[category_model_df["Model"] == "openai:text-davinci-003"]["Correct"],
        color="#FF0000",
        label="text-davinci-003.",
        alpha=0.5,
        # set the bar width to 0.25
        height=0.075,
    )

    # add text to label the group of bars right above
    matplotlib.pyplot.text(0.18, 4.67, "GPT-3.5", fontsize=14, color="#000000", alpha=1.0)

    # plot the values for 'openai:chat-davinci-003-alpha' side by side
    matplotlib.pyplot.barh(
        numpy.arange(len(category_list)) / 10.0 + 3.0,
        #category_model_df[category_model_df["Model"] == "openai:chat-davinci-003-alpha"]["Correct"],
        category_model_df.loc['openai:chat-davinci-003-alpha', category_list],
        color="#FF0000",
        label="ChatGPT",
        alpha=0.5,
        # set the bar width to 0.25
        height=0.075,
    )

    # add text to label the group of bars right above
    matplotlib.pyplot.text(0.18, 3.67, "ChatGPT", fontsize=14, color="#000000", alpha=1.0)

    # plot the values for 'openai:hidden-gpt-4-model-name' side by side
    # with the NCBE values offset by 1.0 to the right
    matplotlib.pyplot.barh(
        numpy.arange(len(category_list)) / 10.0 + 2.0,
        category_model_df.loc['openai:hidden-gpt-4-model-name', category_list],
        color="#00FF00",
        label="GPT-3 Average",
        alpha=0.5,
        # set the bar width to 0.25
        height=0.075,
    )

    # add text to label the group of bars right above
    matplotlib.pyplot.text(0.18, 2.67, "GPT-4", fontsize=14, color="#000000", alpha=1.0)

    # next, plot the values for 'openai:text-davinci-003' side by side
    # with the NCBE values offset by 0.1 to the right
    matplotlib.pyplot.barh(
        numpy.arange(len(category_list)) / 10.0 + 1.0,
        numpy.array(ncbe_correct_rates),
        color="#0000FF",
        label="Student Average",
        alpha=0.5,
        # set the bar width to 0.25
        height=0.075,
    )

    # add text to label the group of bars right above
    matplotlib.pyplot.text(0.18, 1.67, "Student Average", fontsize=14, color="#000000", alpha=1.0)

    tick_positions = numpy.concatenate([
        numpy.arange(len(category_list)) / 10.0 + 1.0,
        numpy.arange(len(category_list)) / 10.0 + 2.0,
        numpy.arange(len(category_list)) / 10.0 + 3.0,
        numpy.arange(len(category_list)) / 10.0 + 4.0,
    ])

    # add xlabels for these ticks as letters A-G
    matplotlib.pyplot.yticks(
        tick_positions,
        list(category_list) * 4,
        fontsize=11,
        # vertical
        rotation=0,
    )

    # add a color legend
    matplotlib.pyplot.legend(
        handles=[
            matplotlib.patches.Patch(color="#FF0000", label="GPT<=3.5 Family", alpha=0.5),
            matplotlib.patches.Patch(color="#00FF00", label="GPT-4", alpha=0.5),
            matplotlib.patches.Patch(color="#0000FF", label="Student Average\n(NCBE BarNow)", alpha=0.5),
        ],
        # put it on the bottom center below the figure
        bbox_to_anchor=(0.825, -0.04),
        ncol=3,
        frameon=False,
        fontsize=14
    )

    # get some more padding on the left for the long labels
    matplotlib.pyplot.subplots_adjust(left=0.25)

    # padding at the bottom for the legend
    matplotlib.pyplot.subplots_adjust(bottom=0.175)

    # add ticks at 10% and label by %s
    matplotlib.pyplot.xticks(
        numpy.arange(0.0, 1.1, 0.1),
        [f"{x * 100:.0f}%" for x in numpy.arange(0.0, 1.1, 0.1)],
        fontsize=11,
    )

    # make tight layout and remove whitespace
    matplotlib.pyplot.tight_layout()

    return fig


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
        # 'hidden
        'openai:hidden-gpt-4-model-name',
        'openai:chat-davinci-003-alpha',
        'openai:text-davinci-003',
    ]

    # Show Top Two Correct Rate by Model and Category but only two digits of precision
    table_df = df.loc[df["Model"].isin(model_filter_list)].groupby(["Question Category", "Model"])["Correct"].mean().unstack()

    # change the table column order to match the list
    table_df = table_df[model_filter_list]

    # plot the figure
    fig = plot_category_bar_chart(df)

    # save to png
    figure_path = Path(__file__).parent/ "figures"

    # create if not exists
    figure_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path / "figure1.png", dpi=300)
