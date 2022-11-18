# Webpage Monitor

A script to check for changes in a webpage once or continuously.

## Configs:
URL_TO_MONITOR - Specifies URL to monitor.
REFRESH_RATE_SECONDS - Determines frequency of checks.

## Usage:
Prior to running the script to check for changes only once, a local
copy of the websites HTML needes to be created. Run "main.py -h" for details.

No prior steps are needed to continuously check for changes.

## Check for changes once
A good use case for this is if one would want to see if a specific webpage has
been updated everytime a terminal is opened. In this case, just call this
script from your .bashrc.
