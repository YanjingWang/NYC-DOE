class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0
        
        max_len = 0
        i = 1
        while i < len(arr) - 1:
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right+1]:
                    right += 1
                max_len = max(max_len, right - left + 1)
                i = right
            else:
                i += 1
        return max_len
    
if __name__ == "__main__":
    print(Solution().longestMountain([2,1,4,7,3,2,5]))
    print(Solution().longestMountain([2,2,2]))
    print(Solution().longestMountain([1,2,3,4,5,6,7,8,9]))
    print(Solution().longestMountain([9,8,7,6,5,4,3,2,1]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]))
    print(Solution().longestMountain([1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))