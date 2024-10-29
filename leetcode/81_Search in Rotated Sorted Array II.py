import typing
class Solution:
    def search(self, nums: typing.List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False
#test code
if __name__ == "__main__":
    test = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    print(test.search(nums, target)) # True
    nums = [2,5,6,0,0,1,2]
    target = 3
    print(test.search(nums, target)) # False
    nums = [1,0,1,1,1]
    target = 0
    print(test.search(nums, target)) # True