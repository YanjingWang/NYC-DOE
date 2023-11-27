class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            return 1 if s != '0' else 0
        dp = [0] * n
        dp[0] = 1 if s[0] != '0' else 0
        if s[1] != '0':
            dp[1] += dp[0]
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
    
test = Solution()
print(test.numDecodings('12'))
print(test.numDecodings('226'))
print(test.numDecodings('0'))