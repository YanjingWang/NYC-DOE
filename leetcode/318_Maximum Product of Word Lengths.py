import typing
class Solution:
    def maxProduct(self, words: typing.List[str]) -> int:
        if not words:
            return 0
        words.sort(key=lambda x: len(x), reverse=True)
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) * len(words[j]) <= ans:
                    break
                if not set(words[i]) & set(words[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

test = Solution()
print(test.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(test.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(test.maxProduct(["a","aa","aaa","aaaa"]))
print(test.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))