class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

if __name__ == '__main__':
    test = Solution()
    print(test.isPowerOfThree(27))
    print(test.isPowerOfThree(0))
    print(test.isPowerOfThree(9))
    print(test.isPowerOfThree(45))