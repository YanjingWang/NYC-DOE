import typing
class Solution:
    def findDisappearedNumbers(self, nums: typing.List[int]) -> typing.List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
if __name__ == "__main__":
    test = Solution()
    print(test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(test.findDisappearedNumbers([1,1]))
    print(test.findDisappearedNumbers([1,2,2,3,3,4,7,8]))
