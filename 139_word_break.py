class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # 1. dp[i]meanss[:i]can be broken or not
        # 2. dp[i] = dp[j] and s[j:i] in wordDict
        # 3. dp[0] = True
        # 4. return dp[-1]
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
#test code
s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))
s = "applepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))

    