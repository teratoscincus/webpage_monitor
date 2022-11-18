"""Module defining the functions to check for changes in a webpage."""

import requests
from time import sleep


def is_webpage_changed(url: str, comparison_state: str) -> bool:
    """
    Return boolean value depending on whether specified webpage has changed or not.

    Params:
        url - Takes a string value of URL to monitor as an argument.
        comparison_state - Takes a string of a webpage HTML as an argument.
    """
    # Get latest webpage content.
    response = requests.get(url)
    latest_webpage_state = response.text

    # Check for changes.
    if latest_webpage_state != comparison_state:
        return True
    else:
        return False


def continuously_check_webpage_changes(url: str, refresh_rate: int = 86_400):
    """
    Continuously check for changes in specified webpage.

    Params:
        url - Takes a string value of URL to monitor as an argument.
        refresh_rate (optional) - Takes an integer values of seconds to wait before
            attempting another get request.
            Defaults to 86,400 seconds (24 hours).
    """
    # Get webpage content to use for comparison.
    response = requests.get(url)
    comparison_webpage_state = response.text

    # Init loop to check if webpage has changed.
    while True:
        sleep(refresh_rate)

        try:
            # Try to get a response.
            is_changed = is_webpage_changed(url, comparison_webpage_state)
        except:
            # Account for lost connection.
            print("Unable to get a response")
            continue

        # Checking successful response for changes.
        if is_changed:
            print("A change has been detected")

            # Update state used for comparison.
            response = requests.get(url)
            comparison_webpage_state = response.text

        else:
            print("...")
