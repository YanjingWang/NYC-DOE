import typing
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: typing.List[int], inorder: typing.List[int]) -> typing.Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root
    # how to print above tree
    def printTree(root):
       if not root:
          return print(root.val)

#    

if __name__ == '__main__':
    test = Solution()
    print(test.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print(test.buildTree([-1], [-1]))
    print(test.buildTree([1,2], [1,2]))
    print(test.buildTree([1,2,3], [3,2,1]))