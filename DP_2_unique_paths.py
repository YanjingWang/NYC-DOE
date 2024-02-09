"""
there is a grid m*n, find the number of unique paths from top left to bottom right (m-1, n-1)
last step: from top left to bottom right, there are two ways to reach the bottom right: move down or move right
previous step location: (m-2, n-1) or (m-1, n-2)
subproblem: from top left to bottom right, there are two ways to reach the bottom right: move down or move right
dp[i][j] = dp[i-1][j] + dp[i][j-1]
initial condition: dp[0][j] = 1, dp[i][0] = 1
return dp[m-1][n-1]

if there are X ways to reach (m-2, n-1) and Y ways to reach (m-1, n-2), then there are X+Y ways to reach (m-1, n-1)
Why X+Y? because it's impossible to reach (m-1, n-2) from other locations
"""
