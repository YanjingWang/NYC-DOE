#leetcode 769. Max Chunks To Make Sorted
import typing
class Solution:
    def maxChunksToSorted(self, arr: typing.List[int]) -> int:
        if not arr:
            return 0
        # 1. find the max value of the current chunk
        # 2. if the max value equals to the current index, then we can split the array
        # 3. if the max value is not equal to the current index, then we need to merge the current chunk with the next chunk
        # 4. return the number of chunks
        max_value = 0
        count = 0
        for i in range(len(arr)):
            max_value = max(max_value, arr[i])
            if max_value == i:
                count += 1
        return count
    
if __name__ == "__main__":
    test = Solution()
    arr = [4,3,2,1,0]
    print(test.maxChunksToSorted(arr)) # 1
    arr = [1,0,2,3,4]
    print(test.maxChunksToSorted(arr)) # 4
    arr = [1,2,0,3]
    print(test.maxChunksToSorted(arr)) # 2
    arr = [0,1,2,3,4]
    print(test.maxChunksToSorted(arr)) # 5


