class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                res += 1
                left = i - 1
                right = i + 2
                while left >= 0 and right < len(s) and s[left] == s[i] and s[right] == s[i + 1]:
                    res += 1
                    left -= 1
                    right += 1
        return res

#testing above code
input = Solution()
print(input.countBinarySubstrings('00110011'))
print(input.countBinarySubstrings('10101'))