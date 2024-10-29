class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            res.append([nums[i]])
            for j in range(i+1, len(nums)):
                res.append([nums[i], nums[j]])
                for k in range(j+1, len(nums)):
                    res.append([nums[i], nums[j], nums[k]])
        res.append([])
        return res
        # res = [[]]
        # for i in nums:
        #     res += [j + [i] for j in res]
        # return res
    
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))