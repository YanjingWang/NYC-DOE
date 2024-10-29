class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1
    
if __name__ == "__main__":
    test = Solution()
    print(test.strStr("hello", "ll"))
    print(test.strStr("aaaaa", "bba"))
    print(test.strStr("", ""))
    print(test.strStr("a", "a"))
    print(test.strStr("mississippi", "issip"))