import typing
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(num2[j]) - ord('0')
                j -= 1
            result = str(sum % 10) + result
            carry = sum // 10
        if carry:
            result = str(carry) + result
        return result
    
if __name__ == "__main__":
    test = Solution()
    num1 = "123"
    num2 = "456"
    print(test.addStrings(num1, num2))