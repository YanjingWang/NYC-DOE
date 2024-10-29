class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
            
        # 1. Find the first decreasing element from the right
        # 2. Find the smallest element greater than the first decreasing element
        # 3. Swap the two elements
        # 4. Reverse the elements from the first decreasing element to the end

        # 1. Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find the smallest element greater than the first decreasing element
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # 3. Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]

        # 4. Reverse the elements from the first decreasing element to the end
        nums[i + 1:] = nums[i + 1:][::-1]

        return nums
    
if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().nextPermutation(nums))
    # [1, 3, 2]
    
    nums = [3, 2, 1]
    print(Solution().nextPermutation(nums))
    # [1, 2, 3]
    
    nums = [1, 1, 5]
    print(Solution().nextPermutation(nums))
    # [1, 5, 1]
    
    nums = [1]
    print(Solution().nextPermutation(nums))
    # [1]
    
    nums = [1, 3, 2]
    print(Solution().nextPermutation(nums))
    # [2, 1, 3]
    
    nums = [2, 3, 1]
    print(Solution().nextPermutation(nums))
    # [3, 1, 2]
    
    nums = [1, 5, 1]
    print(Solution().nextPermutation(nums))
    # [5, 1, 1]
    
    nums = [1, 2, 3, 4, 5]
    print(Solution().nextPermutation(nums))
    # [1, 2, 3, 5, 4]
    
    nums = [1, 2, 3, 5, 4]
    print(Solution().nextPermutation(nums))
    # [1, 2, 4, 3, 5]
    
    nums = [1, 2, 4, 3, 5]
    print(Solution().nextPermutation(nums))
    # [1, 2, 4, 5, 3]
    
    nums = [1, 2, 4, 5, 3]
    print(Solution().nextPermutation(nums))
    # [1, 2, 5, 3, 4]
    
    nums = [1, 2, 5, 3, 4]
    print(Solution().nextPermutation(nums))
    # [1, 2, 5, 4, 3]
    
    nums = [1, 2, 5, 4, 3]
    print(Solution().nextPermutation(nums))
    # [1, 3,