# Define the game tree structure and values based on the given image
game_tree = {
    '1': {'value': None, 'is_terminal': False, 'children': ['2', '3']},
    '2': {'value': None, 'is_terminal': False, 'children': ['4', '5']},
    '3': {'value': None, 'is_terminal': False, 'children': ['6', '7']},
    '4': {'value': None, 'is_terminal': False, 'children': ['8', '9']},  
    '5': {'value': None, 'is_terminal': False, 'children': ['10', '11']},
    '6': {'value': None, 'is_terminal': False, 'children': ['12']},
    '7': {'value': None, 'is_terminal': False, 'children': ['13', '14']},
    # ... Continue for all nodes based on your game tree
    '8': {'value': None, 'is_terminal': False, 'children': ['15', '16']},
    '9': {'value': None, 'is_terminal': False, 'children': ['17']},
    '10': {'value': None, 'is_terminal': False, 'children': ['18', '19']},
    '11': {'value': None, 'is_terminal': False, 'children': ['20']},
    '12': {'value': None, 'is_terminal': False, 'children': ['21']},  
    '13': {'value': None, 'is_terminal': False, 'children': ['22']},
    '14': {'value': None, 'is_terminal': False, 'children': ['23']},
    '15': {'value': -0.9, 'is_terminal': True, 'children': []},
    '16': {'value': -0.8, 'is_terminal': True, 'children': []},
    '17': {'value': -1.0, 'is_terminal': True, 'children': []},
    '18': {'value': 0.0, 'is_terminal': True, 'children': []},
    '19': {'value': 0.0, 'is_terminal': True, 'children': []},
    '20': {'value': -1.0, 'is_terminal': True, 'children': []},
    '21': {'value': 0.7, 'is_terminal': True, 'children': []},
    '22': {'value': -1.0, 'is_terminal': True, 'children': []},
    '23': {'value': -1.0, 'is_terminal': True, 'children': []}, # Terminal nodes have actual values
}

# Populate the terminal nodes with values from the image
game_tree['15']['value'] = -0.9  # Example value, replace with actual value from the image
game_tree['16']['value'] = -0.8  # Example value, replace with actual value from the image
game_tree['17']['value'] = -1.0  # Example value, replace with actual value from the image
game_tree['18']['value'] = 0.0   # Example value, replace with actual value from the image
game_tree['19']['value'] = 0.0   # Example value, replace with actual value from the image
game_tree['20']['value'] = -1.0  # Example value, replace with actual value from the image
game_tree['21']['value'] = 0.7   # Example value, replace with actual value from the image
game_tree['22']['value'] = -1.0  # Example value, replace with actual value from the image
game_tree['23']['value'] = -1.0  # Example value, replace with actual value from the image
# ... Continue for all terminal nodes

# Define the minimax function with alpha-beta pruning as provided earlier to answer Q3.1, Q3.2, and Q3.5
# def minimax(node, depth, maximizing_player, alpha, beta, game_tree):
#     if depth == 0 or node not in game_tree or game_tree[node]['is_terminal']:
#         return game_tree[node]['value']
    
#     if maximizing_player:
#         max_eval = float('-inf')
#         for child in game_tree[node]['children']:
#             eval = minimax(child, depth - 1, False, alpha, beta, game_tree)
#             max_eval = max(max_eval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for child in game_tree[node]['children']:
#             eval = minimax(child, depth - 1, True, alpha, beta, game_tree)
#             min_eval = min(min_eval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 break
#         return min_eval
# Define the minimax function with alpha-beta pruning as provided earlier to answer Q3.4
def minimax(node, depth, maximizing_player, alpha, beta, game_tree, node_count):
    node_count[0] += 1  # Increment the counter each time a node is evaluated
    if depth == 0 or node not in game_tree or game_tree[node]['is_terminal']:
        return game_tree[node]['value']
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in game_tree[node]['children']:
            eval = minimax(child, depth - 1, False, alpha, beta, game_tree, node_count)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in game_tree[node]['children']:
            eval = minimax(child, depth - 1, True, alpha, beta, game_tree, node_count)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    
def calculate_depth(node_id, parent_depth, game_tree):
    # Base case: if the node is terminal, its depth is the parent's depth + 1
    if game_tree[node_id]['is_terminal']:
        return parent_depth + 1
    # Recursive case: go through the children and calculate their depths
    children_depths = [calculate_depth(child, parent_depth + 1, game_tree) for child in game_tree[node_id]['children']]
    # Return the maximum depth found for the children
    return max(children_depths) if children_depths else parent_depth + 1

# # Calculate the depth of the root node
# root_depth = calculate_depth('1', -1, game_tree)
# print(f"Depth of the root node: {root_depth}") # Output: 4

# # Example call to the minimax function (replace 'depth' with actual depth of your tree)
# root_value = minimax('1', depth=4, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 1 (root): {root_value}") 

# # You can call the minimax function for other nodes as required for your questions
# # For example, to find the value for node 2:
# value_node_2 = minimax('2', depth=3, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 2: {value_node_2}")

# # Continue with this approach for other non-terminal nodes as required
# value_node_3 = minimax('3', depth=3, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 3: {value_node_3}")

# value_node_4 = minimax('4', depth=2, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 4: {value_node_4}")

# value_node_5 = minimax('5', depth=2, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 5: {value_node_5}")

# value_node_6 = minimax('6', depth=2, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 6: {value_node_6}")

# value_node_7 = minimax('7', depth=2, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 7: {value_node_7}")

# value_node_8 = minimax('8', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 8: {value_node_8}")

# value_node_9 = minimax('9', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 9: {value_node_9}")

# value_node_10 = minimax('10', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 10: {value_node_10}")

# value_node_11 = minimax('11', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 11: {value_node_11}")

# value_node_12 = minimax('12', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 12: {value_node_12}")    

# value_node_13 = minimax('13', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 13: {value_node_13}")

# value_node_14 = minimax('14', depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 14: {value_node_14}")

# value_node_15 = minimax('15', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 15: {value_node_15}")

# value_node_16 = minimax('16', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 16: {value_node_16}")

# value_node_17 = minimax('17', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 17: {value_node_17}")

# value_node_18 = minimax('18', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 18: {value_node_18}")

# value_node_19 = minimax('19', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 19: {value_node_19}")

# value_node_20 = minimax('20', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 20: {value_node_20}")

# value_node_21 = minimax('21', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 21: {value_node_21}")

# value_node_22 = minimax('22', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 22: {value_node_22}")

# value_node_23 = minimax('23', depth=0, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree)
# print(f"Value for node 23: {value_node_23}")

# Value for node 1 (root): -0.9
# Value for node 2: -0.9
# Value for node 3: -1.0
# Value for node 4: -0.9
# Value for node 5: 0.0
# Value for node 6: 0.7
# Value for node 7: -1.0
# Value for node 8: -0.9
# Value for node 9: -1.0
# Value for node 10: 0.0
# Value for node 11: -1.0
# Value for node 12: 0.7
# Value for node 13: -1.0
# Value for node 14: -1.0
# Value for node 15: -0.9
# Value for node 16: -0.8
# Value for node 17: -1.0
# Value for node 18: 0.0
# Value for node 19: 0.0
# Value for node 20: -1.0
# Value for node 21: 0.7
# Value for node 22: -1.0
# Value for node 23: -1.0

#List all the nodes that will be pruned (i.e., will not need to be evaluated) into the correct category, if we were to run the minimax algorithm with alpha-beta pruning.
#Pruned nodes are those that are not evaluated because their value does not affect the final result.
#The algorithm uses alpha-beta pruning to avoid evaluating nodes that cannot affect the final result.
#The nodes that will be pruned are:
#Node 9
#Node 11
#Node 13
#Node 14
#Node 17
#Node 20
#Node 22
#Node 23
#These nodes will be pruned because their values do not affect the final result of the minimax algorithm due to the use of alpha-beta pruning. Why? Because their values do not change the alpha and beta values, so the algorithm can safely ignore them.

# To count the number of nodes evaluated, you could modify the minimax function to increment a counter each time a node is evaluated.

    
# Example call to the minimax function with node count
node_count = [0]  # Initialize the counter
root_value = minimax('1', depth=4, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), game_tree=game_tree, node_count=node_count)
print(f"Value for node 1 (root): {root_value}")
print(f"Number of nodes evaluated: {node_count[0]}")  # Output: Number of nodes evaluated: 21



