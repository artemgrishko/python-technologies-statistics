import matplotlib.pyplot as plt

from analize_technologies import get_top_technologies


def technology_histogram():
    counts, tech_labels = get_top_technologies()

    plt.figure(figsize=(10, 6))
    plt.bar(tech_labels, counts, color="skyblue")
    plt.xlabel("Technologies")
    plt.ylabel("Counts")
    plt.title("Technology Counts")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    plt.show()
