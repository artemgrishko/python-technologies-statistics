import pandas as pd


def get_top_technologies():
    data = pd.read_csv("technologies.csv", header=None, names=["technologies"])
    technologies_series = data["technologies"].str.split(",", expand=True).stack()
    technologies_series = technologies_series.str.strip()
    technologies_count = technologies_series.value_counts()

    top_technologies = technologies_count.index[:15].tolist()
    top_counts = technologies_count.values[:15].tolist()

    return top_counts, top_technologies
