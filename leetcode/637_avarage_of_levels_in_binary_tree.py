import typing
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: typing.Optional[typing.TreeNode]) -> typing.List[float]:
        if root is None:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(sum(level) / len(level))
        return result
    
if __name__ == '__main__':
    test = Solution()
    print(test.averageOfLevels([3,9,20,None,None,15,7]))
    print(test.averageOfLevels([3,9,20,15,7]))
    print(test.averageOfLevels([3,9,20,15,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))