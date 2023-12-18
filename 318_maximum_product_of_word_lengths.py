class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word_to_bitmask(word):
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            return mask

        bitmasks = [word_to_bitmask(word) for word in words]
        max_product = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert sol.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0