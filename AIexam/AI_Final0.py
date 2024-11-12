# Python code to compute the fitness function of genetic algorithm children

# Function to compute the total damage
def calculate_total_damage(X):
    # Assuming each gene contributes with these weights to the damage
    weights = [10, 20, 30, 40, 50]
    return sum(w*x for w, x in zip(weights, X))

# Function to compute the variety penalty
def calculate_variety_penalty(X):
    if sum(X) == 0:
        return 0
    return 1000 * (1 - max(X)/sum(X))

# Data for children
child1 = [20, 40, 30, 40, 10]
child2 = [30, 10, 20, 10, 20]
child3 = [30, 30, 20, 10, 20]

# Compute total damage for each child
damage_child1 = calculate_total_damage(child1)
damage_child2 = calculate_total_damage(child2)
damage_child3 = calculate_total_damage(child3)

# Compute variety penalty for each child
variety_child1 = calculate_variety_penalty(child1)
variety_child2 = calculate_variety_penalty(child2)
variety_child3 = calculate_variety_penalty(child3)

# Compute fitness function for each child
fitness_child1 = damage_child1 - variety_child1
fitness_child2 = damage_child2 - variety_child2
fitness_child3 = damage_child3 - variety_child3

print("Fitness Child 1:", fitness_child1)
print("Fitness Child 2:", fitness_child2)
print("Fitness Child 3:", fitness_child3)
