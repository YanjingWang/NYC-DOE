import typing
class Solution:
    def candy(self, ratings: typing.List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
    
test = Solution()
print(test.candy([1,0,2]))
print(test.candy([1,2,2]))
print(test.candy([1,3,2,2,1]))
print(test.candy([1,2,87,87,87,2,1]))