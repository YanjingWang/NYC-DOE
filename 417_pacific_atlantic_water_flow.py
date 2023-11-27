import typing


class Solution:
    def pacificAtlantic(self, heights: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(heights, pacific, i, 0)
            self.dfs(heights, atlantic, i, n-1)
        for j in range(n):
            self.dfs(heights, pacific, 0, j)
            self.dfs(heights, atlantic, m-1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, heights, visited, i, j):
        visited[i][j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]) or visited[x][y] or heights[x][y] < heights[i][j]:
                continue
            self.dfs(heights, visited, x, y)


if __name__ == '__main__':
    test = Solution()
    print(test.pacificAtlantic([[1, 2, 2, 3, 5],
                                [3, 2, 3, 4, 4],
                                [2, 4, 5, 3, 1],
                                [6, 7, 1, 4, 5],
                                [5, 1, 1, 2, 4]]))
    print(test.pacificAtlantic([[1, 2, 3],
                                [8, 9, 4],
                                [7, 6, 5]]))
    print(test.pacificAtlantic([[1, 2, 3],
                                [8, 9, 4],
                                [7, 6, 5],
                                [20, 21, 22]]))
