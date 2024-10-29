# Definition for a binary tree node.
import typing
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: typing.Optional[TreeNode]) -> typing.List[int]:
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(test.preorderTraversal(root)) # [1,2,3]
    root = None
    print(test.preorderTraversal(root)) # []
    root = TreeNode(1)
    print(test.preorderTraversal(root)) # [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(test.preorderTraversal(root)) # [1,2]

