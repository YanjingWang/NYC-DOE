import typing
class Solution:
    def dfs(self, graph, colors, i, color):
        colors[i] = color
        for j in graph[i]:
            if colors[j] == color:
                return False
            if colors[j] == 0 and not self.dfs(graph, colors, j, -color):
                return False
        return True
    def isBipartite(self, graph: typing.List[typing.List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1):
                return False
        return True
#test code
s = Solution()
print(s.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(s.isBipartite([[1],[0,3],[3],[1,2]]))
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))