import typing


class Solution:
    def findMaxForm(self, strs: typing.List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


if __name__ == '__main__':
    test = Solution()
    print(test.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(test.findMaxForm(["10", "0", "1"], 1, 1))
    print(test.findMaxForm(["10", "0001", "111001", "1", "0"], 4, 3))
