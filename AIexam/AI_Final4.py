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

# Define the signals
signalA = [0,0,7,8,6,3,1,0,0,0]
signalB = [0,3,6,8,9,6,7,5,1,0]
signalC = [0,8,9,8,5,4,2,1,0,0]

# Compute DTW distances
dtw_AB = compute_dtw(signalA, signalB)
dtw_AC = compute_dtw(signalA, signalC)
dtw_BC = compute_dtw(signalB, signalC)

# Get the DTW distances from the bottom-right corner of the matrices
distance_AB = dtw_AB[-1, -1]
distance_AC = dtw_AC[-1, -1]
distance_BC = dtw_BC[-1, -1]

print(f"DTW Distance between A and B: {distance_AB}")
print(f"DTW Distance between A and C: {distance_AC}")
print(f"DTW Distance between B and C: {distance_BC}")

#Section 8 Pattern Recognition Part A
def dynamic_warping_distance(a, b):
    n = len(a) # * Y-axis
    m = len (b) # * X-axis
    # * origin start from bottom-left corner
    D = np. zeros ((n, m) )
    for i in range(n):
        for j in range(m):
            # * get temps
            temp = []
            if 1<=i<=n-1:
                temp.append (D[i - 1, j])
            if 1<=j<= m - 1:
                temp.append(D[i, j - 1])
            if (1<=i<=n - 1) and (1 <= j <= m - 1): 
                temp.append (D[i - 1, j - 1])
            D[i, j] = abs(a[i] - b[j])
            if len (temp) > 0:
                D[i, j] += min (temp)
            pass
            # * flip upside down
            D = np.array (D)
            D = np. flipud (D)
    # print(f"DEBUG | DWT =\n{D}")
    return D
# *DEBUG
# A = [4,6,8,8,5,4,3,7]
# B = [3,4,6,9,8,5,2,6]
A = [0,0,7,8,6,3,1,0,0,0]
B = [0,3,6,8,9,6,7,5,1,0]
C = [0,8,9,8,5,4,2,1,0,0]
D55 = dynamic_warping_distance (A, B)
print(f"DEBUG | D55 =\n{D55}")
D56 = dynamic_warping_distance (A, C)
print(f"DEBUG | D56 =\n{D56}")
D66 = dynamic_warping_distance (B, C)
print(f"DEBUG | D66 =\n{D66}")
