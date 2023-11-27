import typing
class Solution:
    def findOrder(self, numCourses: int, prerequisites: typing.List[typing.List[int]]) -> typing.List[int]:
        # 1. build graph
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        # 2. topological sort
        visited = [0] * numCourses
        res = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, res):
                return []
        return res[::-1]
    
    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, res):
                return False
        visited[i] = 1
        res.append(i)
        return True
    

if __name__ == "__main__":
    test = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(test.findOrder(numCourses, prerequisites)) # [0,1]
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(test.findOrder(numCourses, prerequisites)) # [0,2,1,3]