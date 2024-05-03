"""
A: {MR, BR}
C: {FL, FR, ML, MR}
H: {FL, FR, ML, MR, BL, BR}
J: {FR, ML, MR, BL, BR}
L: {FL, ML, MR}
S: {FL, ML, BL}
"""
# Python calculation for the number of complete assignments
domain_sizes = [2, 4, 6, 5, 3, 3]  # Taken from the domain sizes of A, C, H, L, S
total_assignments = 1
for size in domain_sizes:
    total_assignments *= size

print(total_assignments)  # This gives the number of complete assignments
