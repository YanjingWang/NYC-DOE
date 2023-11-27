class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
# test code
s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(3, 1))
print(s.hammingDistance(0, 0))
print(s.hammingDistance(0, 1))
print(s.hammingDistance(1, 1))