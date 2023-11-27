# what does `def __init__(self, val):` mean?  Why use `self`? Why use `val`? Why use `__init__`?
# __init__ is a special method that's automatically called when you create a new instance of a class. It's used to initialize the attributes of the class.
# self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
#BFS: 1. build a graph 2. bfs to find the shortest path 3. dfs to find all the paths 
#when queue is empty, the while loop stops

class TreeNode:
    def __init__(self, val):
        self.val = val  # value can store any data, string, list, value
        self.left = None
        self.right = None


def build_tree():
    node_1 = TreeNode(8) #node_1 is the root node, it is the instance of the class TreeNode
    node_2 = TreeNode(3)
    node_3 = TreeNode(10)
    node_4 = TreeNode(1)
    node_5 = TreeNode(6)
    node_6 = TreeNode(14)
    node_7 = TreeNode(4)
    node_8 = TreeNode(7)
    node_9 = TreeNode(13)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    node_5.left = node_7
    node_5.right = node_8

    node_6.right = node_9

    return node_1  # we know whole tree through the root node


def traverse_tree(root):
    if root is None:
        return  # end case/base case funcs immediately stop running
    print(root.val, end=' ')
    traverse_tree(root.left)  # None doesn't have left or right
    traverse_tree(root.right)  # recursive


def preorder_traverse(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder_traverse(root.left)
    preorder_traverse(root.right)


def inorder_traverse(root):
    if root is None:
        return
    inorder_traverse(root.left)
    print(root.val, end=' ')
    inorder_traverse(root.right)


def postorder_traverse(root):
    if root is None:
        return
    postorder_traverse(root.left)
    postorder_traverse(root.right)
    print(root.val, end=' ')


if __name__ == '__main__':
    root = build_tree()
    traverse_tree(root)
    # preorder_traverse(root)
    inorder_traverse(root)
    postorder_traverse(root)
