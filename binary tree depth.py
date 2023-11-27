class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution():
    def maxDepth(self, root):
        self.res = 0
        self.helper(root,1)
        return self.res

    def helper(self, root, height):
        if root is None:  # if not root
            return
        self.res = max(self.res, height)
        # if root.left is None and root.right is None:
        #     self.res += root.val
        self.helper(root.left, height + 1)
        self.helper(root.right, height + 1 )

    # def build_tree(self):
    #     self.node_1 = TreeNode(8)
    #     self.node_2 = TreeNode(3)
    #     self.node_3 = TreeNode(10)
    #     self.node_4 = TreeNode(1)
    #     self.node_5 = TreeNode(6)
    #     self.node_6 = TreeNode(14)
    #     self.node_7 = TreeNode(4)
    #     self.node_8 = TreeNode(7)
    #     self.node_9 = TreeNode(13)
    #
    #     self.node_1.left = self.node_2
    #     self.node_1.right = self.node_3
    #
    #     self.node_2.left = self.node_4
    #     self.node_2.right = self.node_5
    #
    #     self.node_3.right = self.node_6
    #
    #     self.node_5.left = self.node_7
    #     self.node_5.right = self.node_8
    #
    #     self.node_6.right = self.node_9
    #
    #     return self.node_1  # we know whole tree through the root node
    #
    # def traverse_tree(self,root):
    #     if root is None:
    #         return  # end case/base case funcs immediately stop running
    #     print(root.val, end=' ')
    #     self.traverse_tree(root.left)  # None doesn't have left or right
    #     self.traverse_tree(root.right)  # recursive


test1 = Solution()
test1.leafSum({1, 2, 3, 4, 5})  # 7
#
# if __name__ == '__main__':
#     root = build_tree()
#     traverse_tree(root)
