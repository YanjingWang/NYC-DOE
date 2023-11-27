class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        # 1. DP
        # dp[i] = dp[i-1] + 1 if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]
        # dp[i] = 0 otherwise
        # Time: O(n)
        # Space: O(n)
        # dp = [0] * len(nums)
        # for i in range(2, len(nums)):
        #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        #         dp[i] = dp[i-1] + 1
        # return sum(dp)

        # 2. DP
        # dp = 0
        # for i in range(2, len(nums)):
        #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        #         dp += 1
        # return dp

        # 3. DP
        # dp = 0
        # sum = 0
        # for i in range(2, len(nums)):
        #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        #         dp += 1
        #     else:
        #         dp = 0
        #     sum += dp
        # return sum
    
        # 4. Math
        # Time: O(n)
        # Space: O(1)
        sum = 0
        dp = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
            else:
                dp = 0

            sum += dp
        return sum

# Path: 414_third_maximum_number.py
if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(s.numberOfArithmeticSlices([1, 2, 3, 4, 5]))
    print(s.numberOfArithmeticSlices([1, 2, 3, 4]))