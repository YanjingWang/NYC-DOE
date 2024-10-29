import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
    #     """
    #     :type nums: List[int]
    #     :type threshold: int
    #     :rtype: int
    #     """
            
    #     # Step 1: Find the maximum value in nums
    #     max_val = max(nums)
        
    #     # Step 2: Find the minimum divisor
    #     min_divisor = 1
    #     for divisor in range(1, max_val + 1):
    #         if sum([math.ceil(num / divisor) for num in nums]) <= threshold:
    #             min_divisor = divisor
    #             break
        
    #     return min_divisor
## above cod eis wrong, it outputs 3 for [1,2,5,9], 6 but it should be 5
## below code is correct
    # def smallestDivisor(self, nums, threshold):
    #     """
    #     :type nums: List[int]
    #     :type threshold: int
    #     :rtype: int
    #     """            
    #     # Step 1: Find the maximum value in nums
    #     max_val = max(nums)
        
    #     # Step 2: Find the minimum divisor
    #     min_divisor = 1
    #     left, right = 1, max_val
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if sum([math.ceil(num / mid) for num in nums]) <= threshold:
    #             min_divisor = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1
        
    #     return min_divisor
        def sumDivisions(divisor):
            return sum((num + divisor - 1) // divisor for num in nums)
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            total = sumDivisions(mid)
            
            if total > threshold:
                left = mid + 1
            else:
                right = mid
        
        return left
if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestDivisor([1,2,5,9], 6))
    print(sol.smallestDivisor([2,3,5,7,11], 11))
    print(sol.smallestDivisor([19], 5))

    # def smallestDivisor_binary_search(self, nums, threshold):
    #     """
    #     :type nums: List[int]
    #     :type threshold: int
    #     :rtype: int
    #     """
            
    #     # Step 1: Find the maximum value in nums
    #     max_val = max(nums)
        
    #     # Step 2: Find the minimum divisor
    #     min_divisor = 1
    #     left, right = 1, max_val
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if sum([ceil(num / mid) for num in nums]) <= threshold:
    #             min_divisor = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1
        
    #     return min_divisor
    
