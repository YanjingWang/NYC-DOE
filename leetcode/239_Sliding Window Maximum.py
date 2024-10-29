import typing
class Solution:
    def maxSlidingWindow(self, nums: typing.List[int], k: int) -> typing.List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(test.maxSlidingWindow(nums, k)) # [3,3,5,5,6,7]
    nums = [1]
    k = 1
    print(test.maxSlidingWindow(nums, k)) # [1]