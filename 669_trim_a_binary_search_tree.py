# Definition for a binary tree node.
import typing
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: typing.Optional[TreeNode], low: int, high: int) -> typing.Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # root.val >= low and root.val <= high
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
    

if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    low = 1
    high = 2
    print(test.trimBST(root, low, high)) # [1,null,2]
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    low = 1
    high = 3
    print(test.trimBST(root, low, high)) # [3,2,null,1]
    root = TreeNode(1)
    low = 1
    high = 2
    print(test.trimBST(root, low, high)) # [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    low = 1
    high = 3
    print(test.trimBST(root, low, high)) # [1,null,2]
    