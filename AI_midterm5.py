import random
import math

# Simulate the uniform random number generator U
def U():
    return random.uniform(0, 1)

# Generate a point (x, y) using the function G(U)
def G(U):
    a = U()
    b = U() * 2 * math.pi
    x = a * math.cos(b)
    y = a * math.sin(b)
    return (x, y)

# Q 5.2.1 Probability: Calculate the probability that (x,y) lies in the right semi-circle
def probability_right_semicircle(G, U, trials=1000000):
    count = sum(1 for _ in range(trials) if G(U)[0] > 0)
    return round(count / trials, 6)

# Q 5.2.2 Probability: Calculate the probability that (x,y) lies within a circle of radius 0.5
def probability_within_small_circle(G, U, trials=1000000):
    count = sum(1 for _ in range(trials) if G(U)[0]**2 + G(U)[1]**2 <= 0.25)
    return round(count / trials, 6)

# Q 5.2.3 Probability: Check if G(U) is uniform within the unit circle
def is_uniform_within_unit_circle(G, U, trials=1000000):
    points_inside_circle = sum(1 for _ in range(trials) if G(U)[0]**2 + G(U)[1]**2 <= 1)
    # If G(U) is uniform, approximately pi/4 of the points should be inside the unit circle
    expected_points_inside = trials * math.pi / 4
    return abs(points_inside_circle - expected_points_inside) / trials < 0.01  # Tolerance for randomness

# Calculate probabilities
prob_semicircle = probability_right_semicircle(G, U)
prob_small_circle = probability_within_small_circle(G, U)
uniformity_check = is_uniform_within_unit_circle(G, U)

# Print results
print(f"Probability for Q 5.2.1: {prob_semicircle}")
print(f"Probability for Q 5.2.2: {prob_small_circle}")
print(f"Uniformity check for Q 5.2.3: {'True' if uniformity_check else 'False'}")
