import typing
class Solution:
    def numberOfArithmeticSlices(self, nums: typing.List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().numberOfArithmeticSlices(nums))
