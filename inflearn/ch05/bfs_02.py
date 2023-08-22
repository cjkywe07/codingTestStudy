# Breadth First Search(BFS) - 너비우선탐색

from collections import deque
from binaryTree_01 import bt

def bfs(root):
    if root is None:
        return []

    visited = []
    q = deque()
    q.append(root)

    while q:
        curr = q.popleft()
        visited.append(curr.data)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    
    return visited

print(bfs(bt.root))
