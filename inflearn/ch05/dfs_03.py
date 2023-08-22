# Depth First Search(DFS) - 깊이우선탐색

from binaryTree_01 import bt

def preOrder(curr):
    if curr is None:
        return

    print(curr.data, end = " ")
    preOrder(curr.left)
    preOrder(curr.right)

def inOrder(curr):
    if curr != None:
        inOrder(curr.left)
        print(curr.data, end = " ")
        inOrder(curr.right)

def postOrder(curr):
    if curr != None:
        postOrder(curr.left)
        postOrder(curr.right)
        print(curr.data, end = " ")

preOrder(bt.root)
print()
inOrder(bt.root)
print()
postOrder(bt.root)
