import time
from selenium.webdriver.common.keys import Keys

from game import Game

game = Game()

game.open_browser()

game.get_numbers_by_tile()
game.press_key(Keys.ARROW_UP)
print(game.get_score())

game.get_numbers_by_tile()
game.press_key(Keys.ARROW_RIGHT)
print(game.get_score())

game.get_numbers_by_tile()
game.press_key(Keys.ARROW_DOWN)
print(game.get_score())

game.get_numbers_by_tile()
game.press_key(Keys.ARROW_LEFT)
print(game.get_score())

game.close_browser()
