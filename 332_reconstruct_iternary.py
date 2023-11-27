import typing
class Solution:
    def findItinerary(self, tickets: typing.List[typing.List[str]]) -> typing.List[str]:
        # 1. build graph
        graph = {}
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = []
            graph[ticket[0]].append(ticket[1])
        for key in graph.keys():
            graph[key].sort()
        # 2. dfs
        def dfs(graph, start, path, n):
            if len(path) == n:
                return True
            if start not in graph:
                return False
            for i in range(len(graph[start])):
                dest = graph[start].pop(i)
                path.append(dest)
                if dfs(graph, dest, path, n):
                    return True
                path.pop()
                graph[start].insert(i, dest)
            return False
        path = ["JFK"]
        dfs(graph, "JFK", path, len(tickets) + 1)
        return path
    
if __name__ == '__main__':
    test = Solution()
    print(test.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(test.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))