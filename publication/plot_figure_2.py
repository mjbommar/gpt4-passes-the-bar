# imports
import textwrap
from pathlib import Path

# packages
import numpy
import matplotlib.pyplot
import pandas
import seaborn


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


def plot_accuracy_bar_chart(session_df: pandas.DataFrame) -> matplotlib.pyplot.Figure:
    """Plot the accuracy bar chart with both the NCBE and GPT-3 correct rates by
    Question Category for publication, including the error bars for GPT-3 correct rates
    based on the standard error of the mean.  Make the NCBE bars in a light blue
    and the GPT-3 bars in a light red."""

    # set the font size to 14
    matplotlib.pyplot.rcParams["font.size"] = 12

    # font color to 34343 80%
    matplotlib.pyplot.rcParams["text.color"] = "#000000"

    # set the background color to white
    matplotlib.pyplot.rcParams["figure.facecolor"] = "white"

    # set the axes background color to white
    matplotlib.pyplot.rcParams["axes.facecolor"] = "white"

    # set the axes grid color to white
    matplotlib.pyplot.rcParams["axes.grid"] = False

    # set grid lines to 000000
    matplotlib.pyplot.rcParams["grid.color"] = "#000000"

    # get the NCBE correct rates
    ncbe_correct_rates = [
        NCBE_CATEGORY_CORRECT_RATES[category]
        for category in session_df["Question Category"].unique()
    ]

    # get the GPT-3 correct rates
    gpt_correct_rates = [
        session_df[session_df["Question Category"] == category]["Correct"].mean()
        for category in session_df["Question Category"].unique()
    ]

    # get the standard error of the mean for the GPT-3 correct rates
    gpt_correct_rates_sem = [
        session_df[session_df["Question Category"] == category]["Correct"].sem()
        for category in session_df["Question Category"].unique()
    ]

    # get the categories
    categories = session_df["Question Category"].unique()

    # get the order of categories by NCBE correct rate
    ncbe_order = numpy.argsort(ncbe_correct_rates)

    # set the figure size
    matplotlib.pyplot.figure(figsize=(12, 8))

    # shade the region between 58-62% correct as the passing region
    matplotlib.pyplot.axhspan(0.58, 0.62, color="#000000", alpha=0.1)

    # draw an arrow to the regionf rom the textbox
    matplotlib.pyplot.annotate(
        "Average MBE\nPassing Range",
        xytext=(-0.15, 0.63),
        xy=(-0.55, 0.615),
        ha="center",
        # draw a box around the text
    )

    # set GPT-2 to 0% score, 0% SEM
    gpt2_rate = 0.0
    gpt2_sem = 0.0

    model_correct_rate = session_df.groupby(["Model"])["Correct"].mean()
    model_correct_rate_sem = session_df.groupby(["Model"])["Correct"].sem()

    # add gpt-2 as 0 correct rate for first row in all_model_correct_rate
    all_model_correct_rate = pandas.concat([pandas.Series([gpt2_rate], index=["GPT-2"]), model_correct_rate])
    all_model_correct_rate_sem = pandas.concat([pandas.Series([gpt2_sem], index=["GPT-2"]), model_correct_rate_sem])

    # add the human rates at
    all_model_correct_rate = pandas.concat([all_model_correct_rate, pandas.Series([0.675], index=["Average Student"])])
    all_model_correct_rate_sem = pandas.concat([all_model_correct_rate_sem, pandas.Series([0.0], index=["Average Student"])])

    print(all_model_correct_rate.index)

    # order the model rows by time
    model_order = ['GPT-2',
                   'openai:text-ada-001',
                   'openai:text-babbage-001',
                   'openai:text-curie-001',
                   'openai:text-davinci-001',
                   'openai:text-davinci-003',
                   'openai:chat-davinci-003-alpha',
                   'openai:hidden-gpt-4-model-name',
                   'Average Student']

    all_model_correct_rate = all_model_correct_rate.reindex(model_order)

    # plot the bar chart
    matplotlib.pyplot.bar(
        x=numpy.arange(len(all_model_correct_rate)),
        height=all_model_correct_rate,
        yerr=all_model_correct_rate_sem,
        color=["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#00FF00", "#0000FF"],
        ecolor="#000000",
        capsize=3,
        edgecolor="#000000",
        linewidth=0.5,
        alpha=0.5
    )

    # add a color legend
    matplotlib.pyplot.legend(
        handles=[
            matplotlib.patches.Patch(color="#FF0000", label="GPT<=3.5", alpha=0.5),
            matplotlib.patches.Patch(color="#00FF00", label="GPT-4", alpha=0.5),
            matplotlib.patches.Patch(color="#0000FF", label="NCBE", alpha=0.5),
        ],
        # put it on the bottom center below the figure
        bbox_to_anchor=(0.75, -0.1),
        ncol=3,
        frameon=False,
        fontsize=14
    )

    # create x axis labels
    x_labels = [
        "GPT-2",
        "ada\n001",
        "babbage\n001",
        "curie\n001",
        "davinci\n001",
        "GPT-3.5",
        'ChatGPT',
        "GPT-4",
        "Student Avg.\n(NCBE BarNow)",
    ]

    # set the x axis tick labels
    matplotlib.pyplot.xticks(
        numpy.arange(len(all_model_correct_rate)),
        x_labels,
        ha="center",
    )

    # make y axis percentages from 0-80% by 10s
    matplotlib.pyplot.yticks(numpy.arange(0, 0.81, 0.1))

    # label y axis as %
    matplotlib.pyplot.gca().yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))

    # draw a line between x=5 and x=6 to label Q1 2023
    matplotlib.pyplot.axvline(x=6.5, color="#000000", linestyle="--", linewidth=0.5)
    matplotlib.pyplot.text(
        x=6.175,
        y=0.55,
        s="Q1 2023",
        ha="center",
        va="center",
        color="#000000",
        fontweight="bold",
        fontsize=12,
    )

    # draw a line between x=5 and x=6 to label Q4 2022
    matplotlib.pyplot.axvline(x=4.5, color="#000000", linestyle="--", linewidth=0.5)
    matplotlib.pyplot.text(
        x=4.175,
        y=0.55,
        s="Q4 2022",
        ha="center",
        va="center",
        color="#000000",
        fontweight="bold",
        fontsize=12,
    )

    # do the same thing between x=0 and x=1 for Q1 2019
    matplotlib.pyplot.axvline(x=0.5, color="#000000", linestyle="--", linewidth=0.5)
    matplotlib.pyplot.text(
        x=0.175,
        y=0.55,
        s="Q1 2019",
        ha="center",
        va="center",
        color="#000000",
        fontweight="bold",
        fontsize=12,
    )

    # set the y axis label
    matplotlib.pyplot.ylabel("Correct Rate")

    # add title
    matplotlib.pyplot.title("Progression of GPT Models on the MBE", fontweight="bold", fontsize=20)

    # add x axis label
    #matplotlib.pyplot.xlabel("Model", fontsize=16, labelpad=10)

    # add the 25% random chance rate with -- line 25% #000000
    matplotlib.pyplot.axhline(y=0.25, color="#000000", linestyle="--", linewidth=0.5)

    # add text
    matplotlib.pyplot.text(
        x=-0.175,
        y=0.263,
        s="Random Guessing",
        ha="center",
        va="center",
        color="#000000",
        fontweight="bold",
        fontsize=12,
    )

    # expand figure bounding box
    matplotlib.pyplot.tight_layout()

    return matplotlib.pyplot.gcf()

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

    # subset to only results for GPT-4
    print(df.groupby("Model")["Correct"].mean().sort_values())

    # plot the figure
    fig = plot_accuracy_bar_chart(df)

    # save to png
    figure_path = Path(__file__).parent/ "figures"

    # create if not exists
    figure_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path / "figure2.png", dpi=300)

