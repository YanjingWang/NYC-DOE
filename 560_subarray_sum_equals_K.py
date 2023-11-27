import typing
class Solution:
    def subarraySum(self, nums: typing.List[int], k: int) -> int:
        count = 0
        sum = 0
        hash = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hash:
                count += hash[sum-k]
            if sum in hash:
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1]
    k = 2
    print(test.subarraySum(nums, k))