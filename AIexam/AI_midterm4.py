import math

# Initial temperature
T1 = 1.0  # You can change this as needed

# Define the cooling schedules as functions
def logarithmic_cooling(n, T1):
    return T1 * math.log(2) / math.log(n + 1)

def exponential_cooling(n, T1, gamma=3/4):
    return T1 * (gamma ** n)

def fast_cooling(n, T1):
    return T1 / n

# Find the iteration number where temperature first drops below 0.3
def find_iteration_for_temp_below_target(cooling_func, T1, target_temp=0.3):
    n = 1
    while True:
        Tn = cooling_func(n, T1)
        if Tn < target_temp:
            return n
        n += 1

# Calculate the iteration counts for each cooling schedule
log_iterations = find_iteration_for_temp_below_target(logarithmic_cooling, T1)
exp_iterations = find_iteration_for_temp_below_target(exponential_cooling, T1)
fast_iterations = find_iteration_for_temp_below_target(fast_cooling, T1)

print(f"Logarithmic cooling reaches T=0.3 at iteration: {log_iterations}")
print(f"Exponential cooling reaches T=0.3 at iteration: {exp_iterations}")
print(f"Fast cooling reaches T=0.3 at iteration: {fast_iterations}")

# rank temperature schedules based on the number of iterations to 0 (1, first schedule to reach 0.3, last schedule to approach T=0)
ranked_schedules = sorted([(log_iterations, "logarithmic"), (exp_iterations, "exponential"), (fast_iterations, "fast")])
print(f"Ranking of cooling schedules based on iterations to reach T=0.3: {ranked_schedules}")
