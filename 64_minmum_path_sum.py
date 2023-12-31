import typing


class Solution:
    def minPathSum(self, grid: typing.List[typing.List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        print(dp)
        return dp[m-1][n-1]


if __name__ == '__main__':
    test = Solution()
    print(test.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(test.minPathSum([[1, 2, 3], [4, 5, 6]]))
    print(test.minPathSum([[1, 2], [1, 1]]))
