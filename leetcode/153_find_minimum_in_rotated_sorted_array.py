class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # Method 1: O(n)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        """
        # Method 2: O(logn)
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
    
if __name__ == "__main__":
    test = Solution()
    nums = [4,5,6,7,0,1,2]
    print (test.findMin(nums))
