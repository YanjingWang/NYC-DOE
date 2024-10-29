# Definition for a binary tree node.
import typing
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: typing.Optional[TreeNode], to_delete: typing.List[int]) -> typing.List[TreeNode]:
        if not root:
            return []
        ans = []
        to_delete = set(to_delete)
        def dfs(node, parent, is_left):
            if not node:
                return
            if node.val in to_delete:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                if node.left and node.left.val not in to_delete:
                    ans.append(node.left)
                if node.right and node.right.val not in to_delete:
                    ans.append(node.right)
            dfs(node.left, node, True)
            dfs(node.right, node, False)
        if root.val not in to_delete:
            ans.append(root)
        dfs(root, None, False)
        return ans