"""

The code you provided is a Python function definition for the twoSum function. The class Solution line defines a new class called Solution. The def twoSum(self, nums: List[int], target: int) -> List[int]: line defines a function called twoSum within the Solution class. The function takes three parameters: self, nums, and target. 
The self parameter is a reference to the current instance of the Solution class. The nums parameter is a list of integers. The target parameter is an integer. 
The -> List[int] part of the function definition specifies that the function returns a list of integers.

The -> operator is used in Python to indicate the type of the value that a function returns. In this case, the function returns a list of integers. 
This is useful for static typing, which is a way of checking the types of variables and expressions at compile time. Static typing can help to prevent errors and make code more reliable.

The twoSum function works by iterating through the list nums and finding two numbers that add up to target. If two such numbers are found, the function returns a list containing the indices of the two numbers in the list nums. If no two numbers add up to target, the function returns an empty list.

enumerate(iterable, start=0)

def main():
  nums = [2, 7, 11, 15]
  target = 9
  solution = Solution()
  result = solution.twoSum(nums, target)
  print(result)

if __name__ == "__main__":
  main()  #[0, 1]
"""
from typing import List
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     def get_index(list, i):
    #         for index, item in enumerate(list):
    #             if item == i:
    #                 return index
    #         return -1
    #     i_idx = 0
    #     j_idx = 1
    #     for i in nums:
    #         for j in nums:
    #             if i + j == target:
    #                 return [get_index(nums,i), get_index(nums,j)]
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     i_idx = 0
    #     j_idx = 1
    #     for i,j in zip(nums, nums[1:]):
    #         if i + j == target:
    #             return [i_idx, j_idx]
    #         j_idx += 1
    #     if nums[i_idx] + nums[j_idx] == target:
    #         return [i_idx, j_idx]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # the dictionary num_map is used to keep track of the numbers we've seen so far and their indices.
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
            print(num_map)
        return []
    

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     nums = enumerate(nums)
    #     nums = sorted(nums, key=lambda x:x[1])
    #     l, r = 0, len(nums)-1
    #     while l<r:
    #         if nums[l][1]+nums[r][1] == target:
    #             return [nums[l][0], nums[r][0]]
    #         elif nums[l][1]+nums[r][1] < target:
    #             l += 1
    #         else:
    #             r -= 1
    #     return []
#how to test this code?
# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)

nums = [3,2,4]
target = 6
solution = Solution()
result = solution.twoSum(nums, target)
print(result)

# nums = [3,3]
# target = 6
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)


"""
it doesn't pass below case: so I addd `and i != j` in the if statement
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

""" then it doesn't pass below case: 
Input: nums = [3,3], target = 6
Output: [0,1]
"""