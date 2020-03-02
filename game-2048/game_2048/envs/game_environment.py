import gym
from gym import spaces
import numpy as np
from selenium.webdriver.common.keys import Keys
from game import Game


class Game2048Env(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    ACTION = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

    def __init__(self):
        super(Game2048Env, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=4096, shape=(4, 4, 1), dtype=np.uint8)
        self.game = Game()
        self.done = False
        self.state = None
        self.steps_beyond_done = None

    def step(self, action):
        score_before = self.game.score

        if isinstance(action, int):
            self.game.press_key(self.ACTION[action])
        else:
            self.game.press_key(action)

        self.game.get_numbers_by_tile()
        self.state = self.game.get_numbers()
        score = self.game.score

        if self.game.is_game_over():
            reward = -0.1 / score
            done = True
        else:
            total = (score - score_before)
            if total != 0:
                reward = 0.1 / total
            else:
                reward = 0.1 / 16
            done = False

        for i in range(0, 4):
            if 2048 in self.state[i]:
                reward = 1
                done = True

        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.game.reset()
        self.state = self.game.get_numbers()
        self.steps_beyond_done = None
        self.done = False
        return self.state

    def render(self, mode='human', close=False):
        if close:
            self.game.close_browser()

        return self.game.get_numbers()

    def close(self):
        self.game.close_browser()
