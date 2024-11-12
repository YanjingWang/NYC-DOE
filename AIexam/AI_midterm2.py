import math
import itertools

# # Domains after applying unary constraints
# domains = {
#     'FL': ['Clara', 'Sara', 'Leo'],  # Can't be Ava, Jacob, or Henry
#     'FR': ['Clara', 'Henry', 'Jacob'],  # Can't be Ava, Sara, or Leo
#     'ML': ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara'],  # No constraints
#     'MR': ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara'],  # No constraints
#     'BL': ['Ava', 'Jacob', 'Sara'],  # Can't be Clara, Leo, or Henry
#     'BR': ['Ava', 'Jacob', 'Sara']   # Can't be Clara, Leo, or Henry
# }

# # Q 4.1.1: Calculate the total number of complete assignments (6! since we have 6 people and 6 seats)
# complete_assignments = math.factorial(6)

# # Q 4.1.2: Calculate the complete and consistent assignments
# # To do this, we need to consider all the possible permutations of seat assignments
# # and then filter out the ones that violate the binary constraint (Henry and Jacob must sit in the same row)

# # First, we'll create all possible permutations of seat assignments
# all_possible_permutations = list(itertools.permutations(domains.keys()))

# # Next, we filter permutations where Henry and Jacob sit in the same row (either ML & MR or BL & BR)
# consistent_assignments = [
#     perm for perm in all_possible_permutations
#     if ('Henry' in [perm[2], perm[3]] and 'Jacob' in [perm[2], perm[3]]) or
#        ('Henry' in [perm[4], perm[5]] and 'Jacob' in [perm[4], perm[5]])
# ]

# # The number of consistent assignments is the length of this list
# consistent_assignments_count = len(consistent_assignments)

# # Q 4.1.3.1 to Q 4.1.3.6: These questions ask for the possible values for each variable (seat)
# # The domains dictionary already reflects the possible values after applying unary constraints
# # So we can simply access the values for each key in the domains dictionary to get the possible values

# # Q 4.1.4: Since we have reduced the global constraint into binary constraints, we have only one binary constraint
# # between MR and ML. Thus, there is only one edge in the constraint graph for this constraint.

# # Q 4.1.5: The number of tuples in the set for the constraint edge between FL and FR
# # is the product of the number of possible values for FL and FR after applying unary constraints
# tuples_FL_FR = len(domains['FL']) * len(domains['FR'])

# # Output the answers
# print("Q 4.1.1:", complete_assignments)
# print("Q 4.1.2:", consistent_assignments_count)
# for seat, possible_values in domains.items():
#     print(f"Q 4.1.3.x for {seat}:", possible_values)
# print("Q 4.1.4:", 1)
# print("Q 4.1.5:", tuples_FL_FR)

import itertools

# Domains after applying unary constraints
domains = {
    'FL': ['Clara', 'Sara', 'Leo'],  # Can't be Ava, Jacob, or Henry
    'FR': ['Clara', 'Henry', 'Jacob'],  # Can't be Ava, Sara, or Leo
    'ML': ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara'],  # No constraints
    'MR': ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara'],  # No constraints
    'BL': ['Ava', 'Jacob', 'Sara'],  # Can't be Clara, Leo, or Henry
    'BR': ['Ava', 'Jacob', 'Sara']   # Can't be Clara, Leo, or Henry
}

# Generate all permutations of people that can sit in the front left seat (FL)
permutations_FL = list(itertools.permutations(domains['FL']))
# Generate all permutations of people that can sit in the front right seat (FR)
permutations_FR = list(itertools.permutations(domains['FR']))

# Generate all possible permutations of the people
people = ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara']
all_possible_permutations = list(itertools.permutations(people))

# Filter permutations based on the unary constraints for each seat
# and the binary constraint (Henry and Jacob sitting next to each other in the middle or back row)
def is_valid_permutation(perm):
    return (perm[0] in domains['FL'] and
            perm[1] in domains['FR'] and
            perm[2] in domains['ML'] and
            perm[3] in domains['MR'] and
            perm[4] in domains['BL'] and
            perm[5] in domains['BR'] and
            (('Henry' == perm[2] and 'Jacob' == perm[3]) or ('Henry' == perm[3] and 'Jacob' == perm[2]) or
             ('Henry' == perm[4] and 'Jacob' == perm[5]) or ('Henry' == perm[5] and 'Jacob' == perm[4])))

# Apply the valid_permutation function to filter all possible permutations
valid_permutations = filter(is_valid_permutation, all_possible_permutations)

# Convert the filter object to a list and get the count
consistent_assignments = list(valid_permutations)
consistent_assignments_count = len(consistent_assignments)

# Output the answers
print("Q 4.1.1:", math.factorial(6))  # Total number of complete assignments before constraints
print("Q 4.1.2:", consistent_assignments_count)  # Complete and consistent assignments
# Q 4.1.3: These questions ask for the possible values for each variable (seat)
# The domains dictionary already reflects the possible values after applying unary constraints
# So we can simply access the values for each key in the domains dictionary to get the possible values
for seat, possible_values in domains.items():
    print(f"Q 4.1.3.x for {seat}:", possible_values)

# Q 4.1.4: Since we have reduced the global constraint into binary constraints, we have only one binary constraint
# between ML and MR where Henry and Jacob must sit next to each other. Thus, there is only one edge in the constraint graph for this constraint.
# However, since Henry and Jacob can also sit in BL and BR, there's a second edge to consider.
# Therefore, we have two binary constraints: ML-MR and BL-BR.
print("Q 4.1.4:", 2)

# Q 4.1.5: The number of tuples in the set for the constraint edge between FL and FR
# is the product of the number of possible values for FL and FR after applying unary constraints.
# We multiply the counts since for each person in FL there can be any person in FR (as per the current unary constraints).
tuples_FL_FR = len(domains['FL']) * len(domains['FR'])
print("Q 4.1.5:", tuples_FL_FR)


