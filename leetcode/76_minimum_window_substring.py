class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Get the count of each character in t
        t_count = {}
        for char in t:
            if char not in t_count:
                t_count[char] = 0
            t_count[char] += 1

        # Step 2: Get the count of each character in s
        s_count = {}
        for char in s:
            if char not in s_count:
                s_count[char] = 0
            s_count[char] += 1

        # Step 3: Check if s contains all characters in t
        for char in t_count:
            if char not in s_count or s_count[char] < t_count[char]:
                return ''

        # Step 4: Find the smallest window
        start = 0
        end = len(s) - 1
        for i in range(len(s)):
            if s[i] in t_count:
                start = i
                break
        for i in range(len(s) - 1, -1, -1):
            if s[i] in t_count:
                end = i
                break
        return s[start:end + 1]
    

if __name__ == '__main__':
    test = Solution()
    print(test.minWindow('ADOBECODEBANC', 'ABC'))
    print(test.minWindow('a', 'a'))
    print(test.minWindow('a', 'aa'))
    print(test.minWindow('a', 'b'))
    print(test.minWindow('a', ''))