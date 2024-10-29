class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{:032b}'.format(n)[::-1], 2)
#test code
s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))
print(s.reverseBits(0))
print(s.reverseBits(1))