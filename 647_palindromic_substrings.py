class Solution:
    def __init__(self, count=0):
        self.count = count
    
    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            self.extendPalindrome(s,i,i)
            self.extendPalindrome(s,i,i+1)
        return self.count
    def extendPalindrome(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            self.count+=1
            left-=1
            right+=1

#test run
test = Solution()
print(test.countSubstrings("abc"))
print(test.countSubstrings("aaa"))
print(test.countSubstrings("abba"))