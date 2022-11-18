"""Main entry point for the webpage monitor program."""

from webpage_monitor import continuously_check_webpage_changes

URL_TO_MONITOR = "http://127.0.0.1:5000"
REFRESH_RATE_SECONDS = 10

if __name__ == "__main__":
    continuously_check_webpage_changes(URL_TO_MONITOR, REFRESH_RATE_SECONDS)
