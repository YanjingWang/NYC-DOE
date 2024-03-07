import random
import math

# # Define the uniform random number generator function
# def U():
#     return random.uniform(0, 1)

# # Function to generate points in the square [-1, 1] x [-1, 1]
# def generate_point():
#     return (U() * 2 - 1, U() * 2 - 1)

# # Q 5.1.1 Probability
# # Probability that a point lies in the right semi-circle of the unit circle
# def probability_right_semicircle(num_points=1000000):
#     count = sum(1 for _ in range(num_points) if generate_point()[0] > 0)
#     return count / num_points

# # Q 5.1.2 Probability
# # Probability that a point lies within a smaller circle of radius 0.5
# def probability_within_smaller_circle(num_points=1000000):
#     count = sum(1 for _ in range(num_points) if sum(p**2 for p in generate_point()) <= 0.25)
#     return count / num_points

# # Q 5.1.3 Probability
# # Check if the generated points form a uniform distribution inside a unit square
# def is_uniform_within_unit_square(num_points=1000000):
#     points = [generate_point() for _ in range(num_points)]
#     in_square = all(-1 <= x <= 1 and -1 <= y <= 1 for x, y in points)
#     # Uniform distribution means points are evenly spread throughout the square
#     expected_count = num_points / 4  # Quarter for each quadrant
#     quadrant_count = sum(1 for x, y in points if x >= 0 and y >= 0)
#     return abs(quadrant_count - expected_count) / expected_count < 0.01  # Tolerance

# # Q 5.1.4 Probability
# # Check if the distribution is uniform inside a unit circle
# def is_uniform_within_unit_circle(num_points=1000000):
#     points = [generate_point() for _ in range(num_points)]
#     in_circle = sum(1 for x, y in points if x**2 + y**2 <= 1)
#     # Uniform distribution means points are evenly spread throughout the circle
#     expected_count = num_points * math.pi / 4  # Area of unit circle is pi/4 of the unit square
#     return abs(in_circle - expected_count) / expected_count < 0.01  # Tolerance

# # Calculate probabilities and uniformity
# prob_semicircle = probability_right_semicircle()
# prob_smaller_circle = probability_within_smaller_circle()
# uniform_square = is_uniform_within_unit_square()
# uniform_circle = is_uniform_within_unit_circle()

# # Results
# print(f"Probability for Q 5.1.1: {prob_semicircle:.6f}")
# print(f"Probability for Q 5.1.2: {prob_smaller_circle:.6f}")
# print(f"Uniform distribution check for Q 5.1.3: {'True' if uniform_square else 'False'}")
# print(f"Uniform distribution check for Q 5.1.4: {'True' if uniform_circle else 'False'}")


import random

# Uniform random number generator function
def U():
    return random.uniform(0, 1)

# Function to generate a number in an interval [m,n] using U
def f(m, n):
    return (n - m) * U() + m

# Q 5.1.1 Probability
# Calculate the probability that U' = f(-1, 1) generates a number in the interval [-0.5, 0.5]
def probability_5_1_1():
    trials = 1000000
    count = sum(1 for _ in range(trials) if -0.5 <= f(-1, 1) <= 0.5)
    return round(count / trials, 6)

# Q 5.1.2 Probability
# Probability that (x, y) generated using f(-1, 1) lies within a square with vertices (-0.5, -0.5) to (0.5, 0.5)
def probability_5_1_2():
    trials = 1000000
    count = sum(1 for _ in range(trials) if -0.5 <= f(-1, 1) <= 0.5 and -0.5 <= f(-1, 1) <= 0.5)
    return round(count / trials, 6)

# Q 5.1.3 Probability
# Checking the uniformity of the distribution within the unit square
def check_uniformity_5_1_3():
    trials = 1000000
    points_inside_square = sum(1 for _ in range(trials) if -1 <= f(-1, 1) <= 1 and -1 <= f(-1, 1) <= 1)
    return points_inside_square == trials

# Q 5.1.4 Probability
# Checking the uniformity of the distribution within the unit circle
def check_uniformity_5_1_4():
    trials = 1000000
    points_inside_circle = sum(1 for _ in range(trials) if f(-1, 1)**2 + f(-1, 1)**2 <= 1)
    expected_ratio_inside_circle = math.pi / 4
    actual_ratio_inside_circle = points_inside_circle / trials
    return abs(actual_ratio_inside_circle - expected_ratio_inside_circle) < 0.01  # Allowing some tolerance

# Execute the functions and print the results
prob_5_1_1 = probability_5_1_1()
prob_5_1_2 = probability_5_1_2()
uniformity_square = check_uniformity_5_1_3()
uniformity_circle = check_uniformity_5_1_4()

print(f"Probability for Q 5.1.1: {prob_5_1_1}")
print(f"Probability for Q 5.1.2: {prob_5_1_2}")
print(f"Uniformity within unit square for Q 5.1.3: {uniformity_square}")
print(f"Uniformity within unit circle for Q 5.1.4: {uniformity_circle}")
