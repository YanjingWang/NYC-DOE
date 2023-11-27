import typing
class Solution:
    def combine(self, n: int, k: int) -> typing.List[typing.List[int]]:
        if n < k:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [list(range(1, n+1))]
        result = self.combine(n-1, k)
        for item in self.combine(n-1, k-1):
            item.append(n)
            result.append(item)
        return result
    
if __name__ == '__main__':
    test = Solution()
    print(test.combine(4, 2))  
    print(test.combine(4, 3))
     

        