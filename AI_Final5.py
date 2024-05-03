import numpy as np

def compute_dtw(signal1, signal2):
    n, m = len(signal1), len(signal2)
    dtw_matrix = np.full((n + 1, m + 1), float('inf'))
    dtw_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(signal1[i - 1] - signal2[j - 1])
            dtw_matrix[i, j] = cost + min(dtw_matrix[i - 1, j],    # Insertion
                                         dtw_matrix[i, j - 1],    # Deletion
                                         dtw_matrix[i - 1, j - 1]) # Match
    return dtw_matrix

def extract_path(dtw_matrix):
    i, j = dtw_matrix.shape[0] - 1, dtw_matrix.shape[1] - 1
    path = []
    
    while i > 0 and j > 0:
        path.append((i, j))
        steps = [dtw_matrix[i - 1, j - 1], dtw_matrix[i - 1, j], dtw_matrix[i, j - 1]]
        min_index = np.argmin(steps)
        
        if min_index == 0:
            i, j = i - 1, j - 1
        elif min_index == 1:
            i -= 1
        else:
            j -= 1
    
    # Add the starting point
    path.append((i, j))
    path.reverse()
    
    # Format path for output
    formatted_path = '-'.join(f"{x[0]}-{x[1]}" for x in path)
    return formatted_path

# Define the signals
signalA = [0,0,7,8,6,3,1,0,0,0]
signalB = [0,3,6,8,9,6,7,5,1,0]
signalC = [0,8,9,8,5,4,2,1,0,0]

# Compute DTW matrices
dtw_AB = compute_dtw(signalA, signalB)
dtw_AC = compute_dtw(signalA, signalC)
dtw_BC = compute_dtw(signalB, signalC)

# Extract paths
path_AB = extract_path(dtw_AB)
path_AC = extract_path(dtw_AC)
path_BC = extract_path(dtw_BC)


print(f"Path from A to B: {path_AB}")
print(f"Path from A to C: {path_AC}")
print(f"Path from B to C: {path_BC}")
