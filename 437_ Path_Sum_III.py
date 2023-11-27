import typing
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildtree(self):
        self.node_1 = TreeNode(10)
        self.node_2 = TreeNode(5)
        self.node_3 = TreeNode(-3)
        self.node_4 = TreeNode(3)
        self.node_5 = TreeNode(2)
        self.node_6 = TreeNode(11)
        self.node_7 = TreeNode(3)
        self.node_8 = TreeNode(-2)
        self.node_9 = TreeNode(1)

        self.node_1.left = self.node_2
        self.node_1.right = self.node_3

        self.node_2.left = self.node_4
        self.node_2.right = self.node_5

        self.node_3.right = self.node_6

        self.node_4.left = self.node_7
        self.node_4.right = self.node_8

        self.node_5.right = self.node_9

        return self.node_1
    def pathSum(self, root: typing.Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.res = 0
        self.helper(root, targetSum)
        return self.res
    def helper(self, root, targetSum):
        if root is None:
            return
        self.check(root, targetSum)
        self.helper(root.left, targetSum)
        self.helper(root.right, targetSum)
    def check(self, root, targetSum):
        if root is None:
            return
        if root.val == targetSum:
            self.res += 1
        self.check(root.left, targetSum - root.val)
        self.check(root.right, targetSum - root.val)

test1 = Solution()
root = test1.buildtree()
print(test1.pathSum(root, 8))
print(test1.pathSum(root, 22))
