import typing
class Solution:
    def maxProfit(self, prices: typing.List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            # 0: hold, 1: sold, 2: cooldown
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])
    

if __name__ == "__main__":
    test = Solution()
    prices = [1,2,3,0,2]
    print(test.maxProfit(prices)) # 3
    prices = [1]
    print(test.maxProfit(prices)) # 0
    prices = [1,2]
    print(test.maxProfit(prices)) # 1
        