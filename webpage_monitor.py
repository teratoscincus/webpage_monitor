"""Main entry point for the webpage monitor program."""

import argparse
from pathlib import Path
from time import sleep

from scraper import Scraper
from config import URL_TO_MONITOR, REFRESH_RATE_SECONDS

# Constants required for the program.
BASE_DIR = Path(__file__).resolve().parent

# ClI arguments
parser = argparse.ArgumentParser(
    prog="Webpage Monitor",
    description=(
        "Check for changes in a webpage. Can be run continuously or run once. "
        "A copy of the webpage's state needs to be saved locally before a check can be "
        "done once. This is not needed prior to the continuos check."
    ),
)
# Run continuously
parser.add_argument(
    "-c",
    "--check_continuously",
    nargs="?",
    const=True,
    help=(
        "Runs a scrips to continuously check for updates of a webpage. "
        "No prior steps needed before this execution."
    ),
)
# Run once
parser.add_argument(
    "-o",
    "--check_once",
    nargs="?",
    const=True,
    help=(
        "Compare current webpage state to locally saved copy of previous state. "
        "Must have a locally saved copy of an old state for the website for comparison."
    ),
)
# Parse CLI arguments.
args = parser.parse_args()

# Create Scraper instance.
scraper = Scraper()

if args.check_continuously:
    while True:
        scraper.compare_sources(URL_TO_MONITOR, comparison_path=BASE_DIR)
        sleep(REFRESH_RATE_SECONDS)

elif args.check_once:
    scraper.compare_sources(URL_TO_MONITOR, comparison_path=BASE_DIR)
