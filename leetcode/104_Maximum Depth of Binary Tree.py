import typing
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: typing.Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.left = TreeNode(7)
    print(test.maxDepth(root)) # 3
    root = TreeNode(1)
    print(test.maxDepth(root)) # 1
    root = None
    print(test.maxDepth(root)) # 0
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)
    print(test.maxDepth(root)) # 4
