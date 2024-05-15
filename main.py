import subprocess
from plot_technology_histogram import technology_histogram


def run_all():
    scrape_command = "scrapy crawl technologies -O technologies.csv"
    subprocess.run(scrape_command, shell=True)

    technology_histogram()


if __name__ == "__main__":
    run_all()
