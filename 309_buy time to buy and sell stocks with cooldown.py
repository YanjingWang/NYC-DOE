class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold = 0
        hold = float('-inf')
        rest = 0
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(sold, rest)
    
if __name__ == "__main__":
    print (Solution().maxProfit([1, 2, 3, 0, 2]) )# 3
    print (Solution().maxProfit([1, 2, 4])) # 3
    print (Solution().maxProfit([1, 2, 3, 0, 2])) # 3

