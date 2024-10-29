import typing
class Solution:
    def findRedundantConnection(self, edges: typing.List[typing.List[int]]) -> typing.List[int]:
        # Union Find
        # Time: O(nlogn)
        # Space: O(n)
        # 1. Initialize the parent of each node to itself
        # 2. Iterate through the edges, if the parent of the two nodes are the same, then we found a cycle
        # 3. Otherwise, we union the two nodes
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        parent = [i for i in range(len(edges) + 1)]
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            else:
                union(edge[0], edge[1])
        return []

if __name__ == "__main__":
    test = Solution()
    print(test.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(test.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
    print(test.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5], [2,6], [3,6]]))
    print(test.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5], [2,6], [3,6], [4,7], [5,7]]))