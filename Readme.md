# FrozenLake - Reinforcement Learning with Dynamic Programming
 This Python script demonstrates how to apply Dynamic Programming techniques to solve the FrozenLake environment in OpenAI Gym. The FrozenLake environment is a grid world where the agent navigates through a frozen lake to reach the goal while avoiding holes. The goal is to find an optimal policy that leads to the highest reward.

 ## Requirements
* Python 3.x
* OpenAI Gym

## How to use
1. Install Dependencies: Make sure you have Python 3.x installed. Install the required library using the following command:
```
pip install gym
```
2. Run the script:Execute the script, and it will apply Dynamic Programming (Markov Decision Process) to calculate the optimal policy for the FrozenLake environment.

## Description
1. Environment Initialization: The script sets up the FrozenLake environment with a randomly generated map of size 16. The is_slippery flag determines whether the agent will slip to another cell with a probability of 1/3 in each step.

2. Transition and Reward Matrices: The transition matrix (grid) contains information about transition probabilities, next states, rewards, and termination. The rewards matrix (rewards) is initialized with all zeros, except for the goal cell with a reward of 1.

3. Markov Decision Process (MDP): The script applies the MDP approach to calculate the optimal policy for each cell. It iterates over each cell in reverse order, starting from the goal cell. If a cell is a hole, the reward is set to 0. If a cell is not the goal or hole, the reward is calculated as the maximum of the sum of the neighbor cells' rewards multiplied by the transition probability.

4. Get Action with Maximum Reward: The function get_action() is used to find the action that leads to the maximum reward for the current observation.

5. Iterative Process: The script performs an iterative process to update the rewards matrix until convergence or reaching the maximum number of iterations (max_iter_number). In each iteration, it updates the MDP, chooses the action, performs the action, and updates the current observation.

6. Environment Reset: If the agent reaches the goal or falls into a hole, the environment is reset, and the process continues until the maximum number of iterations is reached.

## Output
 The script aims to find the optimal policy that maximizes the agent's rewards in the FrozenLake environment. The output is not explicitly displayed in this script, but you can observe the agent's progress and the rewards matrix during the iterative process. However, you can modify the script to display additional information or visualize the results.

 ## Credits
 This script was created to demonstrate the use of Dynamic Programming for solving the FrozenLake environment in OpenAI Gym. It can serve as a starting point for more advanced reinforcement learning algorithms and tasks. The FrozenLake environment is part of the OpenAI Gym library.

 Read the complete documentation [HERE](Documentation.pdf).
Also you can read [THIS](Code_review.pdf) code review for more details.