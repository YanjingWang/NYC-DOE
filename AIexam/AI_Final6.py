# def update_q_value(current_q, reward, next_max_q, alpha=0.9, gamma=0.5):
#     """
#     Update the Q-value for a single action using the Q-learning formula:
#     Q(s, a) = Q(s, a) + alpha * [reward + gamma * max(next_state Q-values) - Q(s, a)]
#     """
#     return current_q + alpha * (reward + gamma * next_max_q - current_q)

# # Initial Q-values as provided
# q_table = {
#     (1, 1): {'right': 0, 'down': 0, 'left': 0, 'up': 0},
#     (1, 2): {'right': 0, 'down': 0, 'left': 0, 'up': 0},
#     (2, 1): {'right': 0, 'down': 0, 'left': 0, 'up': 0},
#     (2, 2): {'right': 0, 'down': 0, 'left': 0, 'up': 0},
#     (1, 3): {'right': 0, 'down': 0, 'left': 0, 'up': 0}
# }

# # Q10.B.2: Starting at S you take the following action, move right.
# q_table[(1, 1)]['right'] = update_q_value(q_table[(1, 1)]['right'], -1, max(q_table[(1, 2)].values()))

# # Q10.B.3: Continuing from the cell after the move right you choose the action, move up.
# q_table[(1, 2)]['up'] = update_q_value(q_table[(1, 2)]['up'], -1, max(q_table[(1, 3)].values()))

# # Q10.B.4: Continuing from the cell after the move up you choose the action, move up.
# # Assuming that moving up from (1, 3) leads to the same position, we use a reward based on the problem scenario.
# # No actual next state Q-value change, assuming a placeholder reward.
# q_table[(1, 3)]['up'] = update_q_value(q_table[(1, 3)]['up'], 50, 0)  # Placeholder for the goal state reward

# # Print updated Q-values
# print("Q-values after updates:")
# for state, actions in q_table.items():
#     for action, q_value in actions.items():
#         print(f"State {state} Action {action} -> Q-value: {q_value}")
# Define the Q-table as a dictionary of dictionaries
# Q = {
#     (1, 1): {'Left': 0, 'Right': 3, 'Up': 0, 'Down': 0},
#     (1, 2): {'Left': 0, 'Right': 0, 'Up': 0, 'Down': 2},
#     (1, 3): {'Left': -1, 'Right': 0, 'Up': 0, 'Down': 0},
#     (2, 1): {'Left': 0, 'Right': 0, 'Up': 0, 'Down': 0},
#     (2, 2): {'Left': 0, 'Right': -1, 'Up': 5, 'Down': 0},
#     (2, 3): {'Left': 0, 'Right': 0, 'Up': 0, 'Down': 0},
#     (3, 1): {'Left': 0, 'Right': 0, 'Up': 0, 'Down': 0},
#     (3, 2): {'Left': 0, 'Right': 0, 'Up': 0, 'Down': 0},
#     (3, 3): {'Left': 0, 'Right': -80, 'Up': 0, 'Down': 0}
# }

# # Define the discount factor and learning rate
# gamma = 0.5
# alpha = 0.9

# # Function to update Q-value based on current state, action taken, and reward received
# def update_q(state, action, reward, next_state):
#     # Get the best possible Q-value for the next state
#     max_q_next = max(Q[next_state].values())
#     # Current Q-value for the state and action
#     current_q = Q[state][action]
#     # Bellman equation
#     new_q = current_q + alpha * (reward + gamma * max_q_next - current_q)
#     return new_q

# # Q 10.B.2 Update Q-value for moving right from (1,1)
# reward = 0  # Assuming reward is 0 for moving right
# new_q_value_1_1_right = update_q((1, 1), 'Right', reward, (1, 2))
# Q[(1, 1)]['Right'] = new_q_value_1_1_right

# # Q 10.B.3 Update Q-value for moving up from (1,2)
# reward = 0  # Assuming reward is 0 for moving up
# new_q_value_1_2_up = update_q((1, 2), 'Up', reward, (2, 2))
# Q[(1, 2)]['Up'] = new_q_value_1_2_up

# # Q 10.B.4 Update Q-value for moving up from (2,2)
# reward = 0  # Assuming reward is 0 for moving up
# new_q_value_2_2_up = update_q((2, 2), 'Up', reward, (3, 2))
# Q[(2, 2)]['Up'] = new_q_value_2_2_up

# # Print updated Q-values for verification
# print("Updated Q-value for (1,1) Right:", new_q_value_1_1_right)
# print("Updated Q-value for (1,2) Up:", new_q_value_1_2_up)
# print("Updated Q-value for (2,2) Up:", new_q_value_2_2_up)
