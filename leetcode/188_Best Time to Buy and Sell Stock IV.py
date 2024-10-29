import typing
class Solution:
    def maxProfit(self, k: int, prices: typing.List[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices)//2:
            return self.greedy(prices)
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j]+max_diff)
                max_diff = max(max_diff, dp[i-1][j]-prices[j])
        return dp[-1][-1]
    def greedy(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
# test code
if __name__ == "__main__":
    test = Solution()
    k = 2
    prices = [2,4,1]
    print(test.maxProfit(k, prices)) # 2
    k = 2
    prices = [3,2,6,5,0,3]
    print(test.maxProfit(k, prices)) # 7
    k = 2
    prices = [3,3,5,0,0,3,1,4]
    print(test.maxProfit(k, prices)) # 6
    k = 2