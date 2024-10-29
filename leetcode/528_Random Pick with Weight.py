import typing
class Solution:

    def __init__(self, w: typing.List[int]):
        self.w = w
        self.s = sum(w)
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self) -> int:
        import random
        r = random.randint(1, self.s)
        l, h = 0, len(self.w)-1
        while l < h:
            mid = (l+h)//2
            if self.w[mid] < r:
                l = mid+1
            else:
                h = mid
        return l
        


# Your Solution object will be instantiated and called as such:
w = [1,3]
obj = Solution(w)
param_1 = obj.pickIndex()