import typing
class Solution:
    def summaryRanges(self, nums: typing.List[int]) -> typing.List[str]:
        if not nums:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i-1] == start:
                    res.append(str(start))
                else:
                    res.append(str(start) + '->' + str(nums[i-1]))
                start = nums[i]
        if nums[-1] == start:
            res.append(str(start))
        else:
            res.append(str(start) + '->' + str(nums[-1]))
        return res
    
if __name__ == "__main__":
    test = Solution()
    print(test.summaryRanges([0,1,2,4,5,7]))
    print(test.summaryRanges([0,2,3,4,6,8,9]))
    print(test.summaryRanges([]))
    print(test.summaryRanges([-1]))
    print(test.summaryRanges([0]))