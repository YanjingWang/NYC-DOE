class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
            
        # 1. Initialize
        # 2. Loop
        # 3. Return

        # 1. Initialize
        res = []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1

        # 2. Loop
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # 3. Return
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
    
if __name__ == "__main__":
    print (Solution().majorityElement([3,2,3])) # [3]
    print (Solution().majorityElement([1,1,1,3,3,2,2,2])) # [1, 2]
    print (Solution().majorityElement([1,2])) # [1, 2]
    print (Solution().majorityElement([1,2,2,3,2,1,1,3])) # [1, 2]
