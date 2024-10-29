import typing
class Solution:
    def lengthOfLIS(self, nums: typing.List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([0,1,0,3,2,3]))
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))