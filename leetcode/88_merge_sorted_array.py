import typing
class Solution:
    def merge(self, nums1: typing.List[int], m: int, nums2: typing.List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        # 1. Iterate through nums1 and nums2 from the back
        # 2. Compare the two elements, and put the larger one at the back of nums1
        # 3. If nums2 is not empty, then we put the rest of nums2 into nums1
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif i >= 0:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return
    
if __name__ == "__main__":
    test = Solution()
    print(test.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(test.merge([1,2,3,0,0,0], 3, [2,5,6,7], 4))
    print(test.merge([1,2,3,0,0,0], 3, [2,5,6,7,8], 5))
    