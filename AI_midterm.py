# import math

# # Coordinates for each site
# sites = {
#     'A': (53, 93),
#     'B': (1, 38),
#     'C': (47, 24),
#     'D': (34, 72),
#     'E': (55, 20)
# }

# # Function to calculate the distance between two points
# def distance(site1, site2):
#     x1, y1 = sites[site1]
#     x2, y2 = sites[site2]
#     return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# # Function to calculate the total energy of a path
# def path_energy(path):
#     return sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

# # calculate Acceptance Probability
# def acceptance_probability(energy, new_energy, temperature):
#     if new_energy < energy:
#         return 1
#     return math.exp((energy - new_energy) / temperature)
# # Now you can calculate the energy for each path
# # For example, for the path A-B-C-D-E-A:
# energy = path_energy(['A', 'B', 'C', 'D', 'E', 'A'])
# print(f"The energy for the path A-B-C-D-E-A is: {energy:.6f}") #302.610378

# # And for the path A-B-C-D-E-A -> A-B-E-D-C-A:
# energy = path_energy(['A', 'B', 'E', 'D', 'C', 'A'])
# print(f"The energy for the path A-B-E-D-C-A is: {energy:.6f}") #307.681101



# # And for the path A-B-E-D-C-A -> A-C-E-D-B-A:
# energy = path_energy(['A', 'C', 'E', 'D', 'B', 'A'])
# print(f"The energy for the path A-C-E-D-B-A is: {energy:.6f}") #257.356539
# Acceptance_Probability = acceptance_probability(307.681101, 257.356539, 1)

# # And for the path A-C-E-D-B-A -> A-D-E-C-B-A:
# energy = path_energy(['A', 'D', 'E', 'C', 'B', 'A'])
# print(f"The energy for the path A-D-E-C-B-A is: {energy:.6f}")

# # And for the path A-D-E-C-B-A -> A-D-B-C-E-A:
# energy = path_energy(['A', 'D', 'B', 'C', 'E', 'A'])
# print(f"The energy for the path A-D-B-C-E-A is: {energy:.6f}")


import math

# Coordinates for each site
sites = {
    'A': (53, 93),
    'B': (1, 38),
    'C': (47, 24),
    'D': (34, 72),
    'E': (55, 20)
}

# Function to calculate the distance between two points
def distance(site1, site2):
    x1, y1 = sites[site1]
    x2, y2 = sites[site2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to calculate the total energy of a path
def path_energy(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

# Function to calculate the acceptance probability
def acceptance_probability(delta_E, T):
    if delta_E < 0:
        return 1
    else:
        return math.exp(-delta_E / T)

# Now you can calculate the energy for each path and acceptance probabilities
# Assume the temperature T
T = 1.0

# Define the paths
paths = [
    ['A', 'B', 'C', 'D', 'E', 'A'],
    ['A', 'B', 'E', 'D', 'C', 'A'],
    ['A', 'C', 'E', 'D', 'B', 'A'],
    ['A', 'D', 'E', 'C', 'B', 'A'],
    ['A', 'D', 'B', 'C', 'E', 'A']
]

# Calculate the energies and acceptance probabilities
for i in range(len(paths)-1):
    current_energy = path_energy(paths[i])
    next_energy = path_energy(paths[i+1])
    delta_E = next_energy - current_energy
    accept_prob = acceptance_probability(delta_E, T)
    print(f"Transition from path {i+1} to path {i+2}:")
    print(f"Energy = {next_energy:.6f}, ΔE = {delta_E:.6f}, Acceptance Probability = {accept_prob:.6f}")
