#why use DP: 1. overlapping subproblems 2. optimal substructure 3. store the intermediate results in a table 4. bottom-up or top-down 5. 1D or 2D 6. state transfer function 7. initial state 8. answer 9. time complexity 10. space complexity 
# DP state: recursion tree -> state transfer function -> initial state -> answer f[i] or f[i][j] -> time complexity -> space complexity
# DP function: big problem -> small problem f[i][j] = max/min/sum/or 
# DP initialize: exit condition f[0] or f[0][0] or f[0][i] or f[i][0] or f[i][i]
# DP answer: call recursion f[n-1] or f[n-1][n-1] or f[n-1][0] or f[0][0] or f[0][n-1] or f[n][m] or max(f[n-1][i]) or min(f[n-1][i]) or sum(f[n-1][i])

def minmumTotal(triangle):
    if not triangle:
        return 0
    dp = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
    return dp[0]
def minmumTotal2(triangle): # from where
    n = len(triangle)
    #state: dp[i][j] = min path value from triangle[i][j] to bottom
    dp = [[0] * (i+1) for i in range(n)]
    #initialize: the last row, the destination
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]
    #function:from bottom to top, calculate dp[i][j]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    #answer:starting point
    return dp[0][0]
def minmumTotal3(triangle): # to where
    n = len(triangle)
    #state: dp[i][j] = min path value from triangle[0][0] to [i][j]
    dp = [[0] * (i+1) for i in range(n)]
    # why need to initialize? because we need to compare the value of dp[i-1][j-1] and dp[i-1][j] and some points are not standarded in the triangle
    #initialize: the left and right border because there is no left up corner and right up corner
    dp[0][0] = triangle[0][0]
    #function:dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    #i, j is from i-1,j or i-1,j-1
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    #answer: any point in the last row could be the answer
    return dp[n-1][0]
if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minmumTotal(triangle))
    print(minmumTotal2(triangle))
    print(minmumTotal3(triangle))
