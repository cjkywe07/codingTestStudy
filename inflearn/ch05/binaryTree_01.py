# Binary Tree

class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node('A')
bt.root.left = Node('B')
bt.root.right = Node('C')
bt.root.left.left = Node('D')
bt.root.left.right = Node('E')
bt.root.right.right = Node('F')
bt.root.left.left.left = Node('G')
bt.root.left.left.right = Node('H')
