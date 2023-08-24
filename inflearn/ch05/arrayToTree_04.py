from collections import deque

class TreeNode:
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None

def arrayToTree(arr):
    root = TreeNode(arr[0])
    q = deque()
    q.append(root)

    idx = 1
    while idx < len(arr):
        curr = q.popleft()

        if arr[idx] != None:
            curr.left = TreeNode(arr[idx])
            q.append(curr.left)
        idx += 1

        if idx >= len(arr):
            return root

        if arr[idx] != None:
            curr.right = TreeNode(arr[idx])
            q.append(curr.right)
        idx += 1

    return root
