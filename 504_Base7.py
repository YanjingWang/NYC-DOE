class Solution:
    def convertToBase7(self, num: int) -> str:
        if (num == 0):
            return "0"
        sign = 1
        if (num < 0):
            sign = -1
            num = -num
        result = ""
        while (num > 0):
            result = str(num % 7) + result
            num //= 7
        if (sign == -1):
            result = "-" + result
        return result
    
if __name__ == "__main__":
    test = Solution()
    print(test.convertToBase7(100))
    print(test.convertToBase7(-7))
    print(test.convertToBase7(0))