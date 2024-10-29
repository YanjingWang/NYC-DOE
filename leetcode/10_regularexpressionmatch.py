class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP
        # Time: O(mn)
        # Space: O(mn)
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        
        # initialize dp
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # fill dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                # if p[j-1] is a letter
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][ j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                # if p[j-1] is a '*'
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))

        return dp[m][n]
    
#test code
s = "aab"
p = "c*a*b"
sol = Solution()
print(sol.isMatch(s, p))
