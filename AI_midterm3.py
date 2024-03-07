import itertools

# Define the list of all people
people = ['Ava', 'Clara', 'Henry', 'Jacob', 'Leo', 'Sara']

# Dictionary to hold the potential candidates for each seat after applying unary constraints
candidates = {
    'FL': [person for person in people if person not in ['Ava', 'Jacob', 'Henry', 'Leo']],  # Can't be Ava, Jacob, Henry, or Leo
    'FR': [person for person in people if person not in ['Ava', 'Sara', 'Leo']],            # Can't be Ava, Sara, or Leo
    'BL': [person for person in people if person not in ['Clara', 'Leo', 'Henry']],         # Can't be Clara, Leo, or Henry
    'BR': [person for person in people if person not in ['Clara', 'Leo', 'Henry']],         # Can't be Clara, Leo, or Henry
}

# Generate all possible assignments that respect the unary constraints
def generate_assignments(candidates):
    for perm in itertools.permutations(people):
        if all(perm[i] in candidates[seat] for i, seat in enumerate(['FL', 'FR', 'BL', 'BR'])):
            yield perm

# Count the number of complete and consistent assignments
assignments = list(generate_assignments(candidates))
consistent_assignments_count = len(assignments)

# Determine the least constraining values for FL
# This means finding the person who when assigned to FL leaves the most options for the other seats
def least_constraining_values(candidates, seat):
    lcv = {}
    for candidate in candidates[seat]:
        # Calculate the number of options left for other seats if this candidate is chosen for FL
        remaining_options = 1  # Start with 1 because we are counting combinations
        for other_seat, other_candidates in candidates.items():
            if other_seat != seat:
                remaining_options *= len([oc for oc in other_candidates if oc != candidate])
        lcv[candidate] = remaining_options
    # Return the candidates that are least constraining (have the highest remaining_options)
    max_options = max(lcv.values())
    return [c for c, options in lcv.items() if options == max_options]

lcv_for_FL = least_constraining_values(candidates, 'FL')

# Answer to Q 4.2.1 CSP
print(consistent_assignments_count)

# Answer to Q 4.2.2 CSP
print(lcv_for_FL)
