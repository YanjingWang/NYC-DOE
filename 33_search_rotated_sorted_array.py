class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Solution 1: O(log(n)) time, O(1) space
        # Idea: binary search
        # 1. find the pivot point
        # 2. find the target in the left or right part
        # 3. if not found, return -1
    #     if not nums:
    #         return -1
    #     pivot = self.find_pivot(nums)
    #     if pivot == -1:
    #         return self.binary_search(nums, 0, len(nums)-1, target)
    #     if nums[pivot] == target:
    #         return pivot
    #     if nums[0] <= target:
    #         return self.binary_search(nums, 0, pivot-1, target)
    #     return self.binary_search(nums, pivot+1, len(nums)-1, target)

    # def find_pivot(self, nums):
    #     if nums[0] <= nums[-1]:
    #         return -1
    #     left, right = 0, len(nums)-1
    #     while left <= right:
    #         mid = (left+right)/2
    #         if nums[mid] > nums[mid+1]:
    #             return mid
    #         if nums[mid] < nums[left]:
    #             right = mid-1
    #         else:
    #             left = mid+1
    #     return -1
    
    # def binary_search(self, nums, left, right, target):
    #     while left <= right:
    #         mid = (left+right)/2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] > target:
    #             right = mid-1
    #         else:
    #             left = mid+1
    #     return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
if __name__ == "__main__":
    test = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print (test.search(nums, target))
    
