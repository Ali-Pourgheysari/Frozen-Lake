# import library

import gymnasium as gym

from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import numpy as np

size = 16

# impliment the environment
# if is_slippery is True, then the agent will slip to the other cell with the probability of 1/3
# if is_slippery is False, then the agent will go to the neighbor cell with maximum reward and will always rich the goal
env = gym.make("FrozenLake-v1", desc=generate_random_map(size=size),
               render_mode="human", is_slippery=True)

observation, info = env.reset(seed=42)

max_iter_number = 1000

# get the transition matrix that contains(transition probability, next state, reward, terminated)
grid = env.unwrapped.P
# rewards matrix
rewards = [[0.0 for _ in range(size)] for _ in range(size)]
rewards[size-1][size-1] = 1

# pre-calculate the coordinates of all cells
coords = np.zeros((size*size, 2), dtype=int)
for i in range(size):
    for j in range(size):
        coords[i*size+j] = (i, j)



for _ in range(max_iter_number):

    ##################################

   

    ##################################

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:

        observation, info = env.reset()

env.close()
