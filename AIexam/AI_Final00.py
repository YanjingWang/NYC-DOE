# # import math

# # def calculate_total_damage(x):
# #     # Hypothetical function, needs accurate formula
# #     return sum(x)  # Simple sum, adjust based on actual calculation

# # def variety_penalty(x):
# #     # Hypothetical function, needs specific formula
# #     return max(x) - min(x)  # Difference between max and min values

# # # Initial conditions
# # x = [5, 5, 10, 10, 10]  # Initial army composition
# # T = 100  # Initial temperature
# # alpha = 0.95  # Cooling rate
# # E_prev = calculate_total_damage(x) - variety_penalty(x)  # Initial E value

# # # Iterations based on the problem statement
# # operations = [
# #     [10, 10, 0, 5, 0],
# #     [-5, 5, 5, -5, -5],
# #     [5, 5, 5, 5, 5],
# #     [5, -5, -5, 10, 5],
# #     [5, 5, 5, -5, 10]
# # ]

# # print(f"Iteration 0: E = {E_prev:.6f}, ΔE = 0.000000, P(accept) = None")  # Output for iteration 0

# # for i, op in enumerate(operations):
# #     x = [x[j] + op[j] for j in range(5)]
# #     E_new = calculate_total_damage(x) - variety_penalty(x)
# #     delta_E = E_prev - E_new  # Adjust sign based on your scenario requirements
    
# #     if delta_E < 0:
# #         P_accept = math.exp(delta_E / T)
# #     else:
# #         P_accept = 1
    
# #     print(f"Iteration {i+1}: E = {E_new:.6f}, ΔE = {delta_E:.6f}, P(accept) = {P_accept:.6f}")
    
# #     E_prev = E_new  # Update E_prev for next iteration's ΔE calculation
# #     T *= alpha  # Update temperature
# import math

# def calculate_damage(x):
#     # Hypothetical function, adjust according to actual scenario
#     return x[0] * 10 + x[1] * 20 + x[2] * 30 + x[3] * 40 + x[4] * 50

# def variety_penalty(x):
#     # Hypothetical variety penalty, adjust accordingly
#     return max(x) - min(x)  # Difference between max and min values

# # Initial conditions
# x = [5, 5, 10, 10, 10]
# T = 100
# alpha = 0.95

# # Initial calculation before operations
# initial_damage = calculate_damage(x)
# initial_penalty = variety_penalty(x)
# E_initial = initial_damage - initial_penalty
# results = [(E_initial, 0, None)]  # ΔE and P(accept) are 0 and None for initial iteration

# # Iterations based on the problem statement
# operations = [
#     [10, 10, 0, 5, 0],
#     [-5, 5, 5, -5, -5],
#     [5, 5, 5, 5, 5],
#     [5, -5, -5, 10, 5],
#     [5, 5, 5, -5, 10]
# ]

# for op in operations:
#     # Apply operation
#     x = [x[i] + op[i] for i in range(5)]
#     damage = calculate_damage(x)
#     penalty = variety_penalty(x)
#     E_new = damage - penalty
#     delta_E = E_new - results[-1][0]  # Calculate ΔE based on the last E value in results
    
#     if delta_E > 0:
#         P_accept = math.exp(-delta_E / T)
#     else:
#         P_accept = 1  # If ΔE <= 0, accept new state with probability 1
    
#     results.append((E_new, delta_E, P_accept))
    
#     # Update temperature
#     T *= alpha

# # Output results for each iteration
# for i, result in enumerate(results):
#     if i == 0:
#         print(f"Iteration {i}: E = {result[0]:.6f}, ΔE = {result[1]}, P(accept) = {result[2]}")
#     else:
#         print(f"Iteration {i}: E = {result[0]:.6f}, ΔE = {result[1]:.6f}, P(accept) = {result[2]:.6f}")
import math

# Initial troop composition and modifications per iteration
initial_composition = [5, 5, 10, 10, 10]
modifications = [
    [10, 0, 0, 5, 0],
    [-5, 5, 5, -5, -5],
    [5, 5, 5, 5, 5],
    [5, -5, -5, 10, 5],
    [5, 5, 5, -5, 10]
]

# Initial temperature and cooling rate
initial_temperature = 100
cooling_rate = 0.95

def calculate_fitness(X):
    # Example fitness function: sum of troops times their damage factor
    damage_factors = [10, 20, 30, 40, 50]  # Hypothetical damage factors
    total_damage = sum(x * d for x, d in zip(X, damage_factors))
    variety_penalty = 1000 * (1 - max(X) / sum(X))  # Variety penalty calculation
    return total_damage - variety_penalty

def update_composition(composition, modification):
    return [x + m for x, m in zip(composition, modification)]

def calculate_temperature(iteration, initial_temp, alpha):
    return initial_temp * alpha ** iteration

def probability_acceptance(delta_e, temperature):
    return math.exp(-delta_e / temperature) if delta_e > 0 else 1

# Start with the initial composition
current_composition = initial_composition.copy()
current_fitness = calculate_fitness(current_composition)
temperatures = [initial_temperature]  # Include initial temperature
fitness_values = [current_fitness]
probabilities = [None]  # No probability of acceptance for the first iteration

# Perform the simulated annealing
for i, modification in enumerate(modifications):
    new_composition = update_composition(current_composition, modification)
    new_fitness = calculate_fitness(new_composition)
    delta_e = new_fitness - current_fitness
    temperature = calculate_temperature(i + 1, initial_temperature, cooling_rate)
    p_accept = probability_acceptance(delta_e, temperature)
    
    # Record the new values
    temperatures.append(temperature)
    fitness_values.append(new_fitness)
    probabilities.append(p_accept)
    
    # Update the current state
    current_composition = new_composition
    current_fitness = new_fitness

# Output the results including iteration 0
print(f"Iteration 0: Temperature = {temperatures[0]:.6f}, Fitness = {fitness_values[0]:.6f}, P(accept) = {probabilities[0]}")
for i, (temp, fit, prob) in enumerate(zip(temperatures[1:], fitness_values[1:], probabilities[1:]), 1):
    print(f"Iteration {i}: Temperature = {temp:.6f}, Fitness = {fit:.6f}, P(accept) = {prob:.6f}")

