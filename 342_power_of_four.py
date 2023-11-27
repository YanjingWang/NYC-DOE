class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True
    
if __name__ == "__main__":
    test = Solution()
    print(test.isPowerOfFour(16))
    print(test.isPowerOfFour(5))
    print(test.isPowerOfFour(1))
    print(test.isPowerOfFour(0))
    print(test.isPowerOfFour(-1))