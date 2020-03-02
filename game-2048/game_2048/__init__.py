from gym.envs.registration import register

register(
    id='game-two-bytes-v0',
    entry_point='game_2048.envs:Game2048Env',
)
