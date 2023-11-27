import typing
class Solution:
    def singleNumber(self, nums: typing.List[int]) -> typing.List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        a = b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
print(Solution().singleNumber([1,2,1,3,2,5])) # [3,5]
print(Solution().singleNumber([-1,0])) # [-1,0]
