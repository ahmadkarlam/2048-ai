from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import numpy as np
import time


class Game:
    def __init__(self):
        self.score = 0
        self.numbers = np.zeros((4, 4))
        self.browser = None
        self.is_browser_open = False

    def get_numbers(self):
        return self.numbers

    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://play2048.co/")
        self.is_browser_open = True
        time.sleep(1)

    def close_browser(self):
        self.browser.close()
        self.is_browser_open = False

    def get_numbers_by_tile(self):
        numbers = np.zeros((4, 4))
        tiles = self.browser.find_elements(By.CLASS_NAME, "tile")
        for tile in tiles:
            classes = tile.get_attribute("class")
            classes = str(classes).replace("tile", "", 1).replace("tile-new", "").replace("tile-merged", "")
            number, location = classes.split()
            number = str(number).replace("tile-", "")
            column, row = str(location).replace("tile-position-", "").split("-")
            numbers[int(row) - 1, int(column) - 1] = int(number)
        self.numbers = numbers

    def set_score(self):
        score = self.browser.find_element(By.CLASS_NAME, "score-container").text
        self.score = int(score)

    def get_score(self):
        return self.score

    def press_key(self, key):
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(key)
        time.sleep(0.7)
        self.set_score()

    def reset(self):
        if self.is_browser_open:
            self.close_browser()
        self.open_browser()
        self.get_numbers_by_tile()

    def is_game_over(self):
        try:
            self.browser.find_element(By.CLASS_NAME, "game-over")
        except NoSuchElementException:
            return False

        return True
