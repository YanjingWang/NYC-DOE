import typing
class Solution:
    def canPartition(self, nums: typing.List[int]) -> bool:
        if len(nums) == 0:
            return True
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
    
if __name__ == "__main__":
    test = Solution()
    print(test.canPartition([1, 5, 11, 5]))
    print(test.canPartition([1, 2, 3, 5]))
    print(test.canPartition([1, 2, 5]))