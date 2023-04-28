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

# Markov Decision Process(policy function)
def MDP():
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            # get the cell number
            cell_number = i * size + j
            # if the cell is the goal, then the reward is 1
            if i == j == 15:
                continue
            # if the cell is the hole, then the reward is 0
            if (grid[cell_number][0][0][1] == cell_number) and (grid[cell_number][0][0][3] == True):
                rewards[i][j] = 0.0
                continue

            # if the cell is not the goal or the hole, then the reward is the sum of the neighbor cells according to the transition probability
            state_list = []
            for k in range(4):
                reward_sum = 0.0
                for item in grid[cell_number][k]:
                    row_index, col_index = coords[item[1]]
                    reward_sum += (1/3) * rewards[row_index][col_index]
                state_list.append(0.9 * reward_sum)
            # get the maximum reward of the neighbor cells
            rewards[i][j] = max(state_list)

# find the action that leads to maximum reward
def get_action():
    row_index, col_index = coords[observation]

    neighbor_indexes = {}
    if col_index - 1 >= 0:
        neighbor_indexes[0] = rewards[row_index][col_index - 1]
    if row_index + 1 < size:
        neighbor_indexes[1] = rewards[row_index + 1][col_index]
    if col_index + 1 < size:
        neighbor_indexes[2] = rewards[row_index][col_index + 1]
    if row_index - 1 >= 0:
        neighbor_indexes[3] = rewards[row_index - 1][col_index]

    max_key = max(neighbor_indexes, key=neighbor_indexes.get)

    return max_key


for _ in range(max_iter_number):

    ##################################

    MDP()
    action = get_action()

    ##################################

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:

        observation, info = env.reset()

env.close()
