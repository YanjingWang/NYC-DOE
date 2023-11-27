class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)
        # return n // 5 + self.trailingZeroes(n // 5) if n >= 5 else 0

test1 = Solution()
print(test1.trailingZeroes(5))  # 1
print(test1.trailingZeroes(3))  # 0
print(test1.trailingZeroes(0))  # 0