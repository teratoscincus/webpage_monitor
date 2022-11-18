"""Main entry point for the webpage monitor program."""

import argparse
from pathlib import Path

from webpage_monitor import (
    continuously_check_webpage_changes,
    is_webpage_changed,
    get_webpage_state,
)

# Configs
URL_TO_MONITOR = "http://127.0.0.1:5000"
REFRESH_RATE_SECONDS = 3

# Constants required for the program.
BASE_DIR = Path(__file__).resolve().parent
COMPARISON_STATE_FILE = BASE_DIR / "previous_webpage_state.txt"

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
    "--check_once",
    nargs="?",
    const=True,
    help=(
        "Compare current webpage state to locally saved copy of previous state. "
        "Must have a locally saved copy of an old state for the website for comparison."
    ),
)
# Get local copy of webpage state for comparison.
parser.add_argument(
    "--get_comparison_state",
    nargs="?",
    const=True,
    help=(
        "Get and save a copy of the current state locally. "
        "Must be done before using the --check_state flag."
    ),
)
# Parse CLI arguments.
args = parser.parse_args()

if args.check_continuously:
    continuously_check_webpage_changes(URL_TO_MONITOR, REFRESH_RATE_SECONDS)

if args.check_once:
    with open(COMPARISON_STATE_FILE, "r") as f:
        comparison_state = f.read()

    try:
        is_changed = is_webpage_changed(URL_TO_MONITOR, comparison_state)
    except:
        # Account for lost connection.
        print("Unable to get a response")
    else:
        if is_changed:
            print("A change has been detected")

            # Update state used for comparison.
            comparison_state = get_webpage_state(URL_TO_MONITOR)
            with open(COMPARISON_STATE_FILE, "w") as f:
                f.write(comparison_state)

        else:
            print("No changes detected")

if args.get_comparison_state:
    comparison_state = get_webpage_state(URL_TO_MONITOR)
    with open(COMPARISON_STATE_FILE, "w") as f:
        f.write(comparison_state)
