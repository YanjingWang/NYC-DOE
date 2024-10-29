import typing


class Solution:
    def rob(self, nums: typing.List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


if __name__ == '__main__':
    test = Solution()
    print(test.rob([1, 2, 3, 1]))
    print(test.rob([2, 7, 9, 3, 1]))
    print(test.rob([2, 1, 1, 2]))
    print(test.rob([2, 1, 1, 2, 1, 1, 2]))
