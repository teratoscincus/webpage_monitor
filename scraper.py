"""Module defining the a class check for changes in a webpage."""

from pathlib import Path
import os

from selenium import webdriver
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True

        self.driver = webdriver.Firefox(options=options)
        # self.driver = webdriver.PhantomJS()  # Requires installation, but is faster.
        self.driver.maximize_window()

    def scrape(self, url):
        self.driver.get(url)
        source = BeautifulSoup(self.driver.page_source)
        self.driver.quit()

        return source

    def compare_sources(self, url, comparison_path):
        # Ensure filename doesn't resemble path structure.
        url_name = url.lstrip("https:/").rstrip("/").replace("/", "#")
        comparison_file_path = comparison_path / f"comparison_{url_name}.html"

        # Check if comparison file exists. Create if not.
        if os.path.exists(comparison_file_path):
            with open(comparison_file_path, "r") as f:
                comparison_file = f.read()
        else:
            with open(comparison_file_path, "w") as f:
                f.write(str(self.scrape(url)))
            print(f"\033[1;33mNo comparison for {url}\nCreating one\033[0m")

        # Compare scrape(url) to comparison file.
        try:
            latest_state = str(self.scrape(url))
        except:
            print("\033[1;33mUnable to get a response\033[0m")

        if latest_state == comparison_file:
            print("\033[1;32mNo changes detected\033[0m")
        else:
            print("\033[1;31mA change has been detected\033[0m")
            print(f"{url}")
