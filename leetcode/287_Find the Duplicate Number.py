#leetcode 287. Find the Duplicate Number
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # phase 1: finding the intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # phase 2: finding the entrance of the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
    
if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))
    # Output: 2
    
    nums = [3,1,3,4,2]
    print(Solution().findDuplicate(nums))
    # Output: 3
    
    nums = [1,1]
    print(Solution().findDuplicate(nums))
    # Output: 1
    
    nums = [1,1,2]
    print(Solution().findDuplicate(nums))
    # Output: 1
    
    nums = [2,2,2,2,2]
    print(Solution().findDuplicate(nums))
    # Output: 2
    
    nums = [2,5,9,6,9,3,8,9,7,1]
    print(Solution().findDuplicate(nums))
    # Output: 9
    
    nums = [1,2,3,4,5,6,7,8,9,9]
    print(Solution().findDuplicate(nums))
    # Output: 9
    
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,9]
    print(Solution().findDuplicate(nums))
    # Output: 9
    
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,9,15]
    print(Solution().findDuplicate(nums))
    # Output: 9
    
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,9,15,16]
    print(Solution().findDuplicate(nums))
    # Output: 9
    
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,9,15,16,17]
            
# Path: 289_Game%20of%20Life.py

        