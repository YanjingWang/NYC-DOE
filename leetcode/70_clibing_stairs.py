class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    test = Solution()
    print(test.climbStairs(4))
    print(test.climbStairs(5))
    print(test.climbStairs(6))
