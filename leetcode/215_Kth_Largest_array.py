import typing
class Solution:
    def findKthLargest(self, nums: typing.List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        # 1. Sort the array
        # 2. Return the kth largest element
        nums.sort()
        return nums[-k]
    
if __name__ == "__main__":
    test = Solution()
    print(test.findKthLargest([3,2,1,5,6,4], 2))
    print(test.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(test.findKthLargest([1], 1)) 
    print(test.findKthLargest([1,2], 2))