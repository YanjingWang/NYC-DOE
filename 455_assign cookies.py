import typing
class Solution:
    def findContentChildren(self, g: typing.List[int], s: typing.List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i+=1
            j+=1
        return i

    def sort(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])
        return self.merge(left,right)

if __name__ == "__main__":
    g = [1,2,3]
    s = [1,1]
    test = Solution()
    # TypeError: Solution.sort() missing 1 required positional argument: 'nums'
    # print(s.sort(g))
    # print(s.findContentChildren(g,s))
    print(test.sort(g))
    print(test.sort(s))
    print(test.findContentChildren(g,s))