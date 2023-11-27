class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        return [left, right]
    
    def find_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
    
    def find_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
    
test1 = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(test1.searchRange(nums, target))
nums = [5,7,7,8,8,10]
target = 6
print(test1.searchRange(nums, target))
nums = []
target = 0
print(test1.searchRange(nums, target))
nums = [1]
target = 1
print(test1.searchRange(nums, target))