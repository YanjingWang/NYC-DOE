class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         # Approach 1
#         # Time: O(n^2)
#         # Space: O(n)
#         res = []
#         for i in range(len(nums)):
#             found = False
#             for j in range(i+1, len(nums)):
#                 if nums[j] > nums[i]: 
#                     res.append(nums[j])
#                     found = True
#                     break
#             if not found:
#                 for j in range(i):
#                     if nums[j] > nums[i]:
#                         res.append(nums[j])
#                         found = True
#                         break
#             if not found:
#                 res.append(-1)

#         return res
    
            # Approach 2
            # Time: O(n)
            # Space: O(n)
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
        return res
    
#         # Approach 3
#         # Time: O(n)
#         # Space: O(n)
#         stack = []
#         res = [-1] * len(nums)
#         for i in range(len(nums)):
#             while stack and nums[stack[-1]] < nums[i]:
#                 res[stack.pop()] = nums[i]
#             stack.append(i)

#         return res

    