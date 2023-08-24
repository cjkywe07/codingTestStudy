# Lowest Common Ancestor of a Binary Tree

'''
문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다.
이 때, 두 노드의 공통 조상 중 가장 낮은 node 즉, the lowest common ancestor(LCA)를 찾아라.
단, 노드는 자기자신의 후손이 될 수 있다.

ex)
    Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
    Output: 3

    Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
    Output: 5

    Input: root = [1, 2], p = 1, q = 2
    Output: 1

제약조건
    2 <= node 개수 <= 10^5
    -10^9 <= Node.val <= 10^9
    모든 Node.val은 Unique하다.
    p != q
    p, q는 모두 주어진 Tree에 속해 있다.
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    0 <= nums.length <= 10^5 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    post order 이용

(3) 코드 설계
    if root == p or q:
        return root
    elif root.left && root.right:
        return root
    elif root.left || root.right:
        return left or right
    elif root.left == None && root.right == None:
        return None

(4) 코드 구현
'''

# ------------------------------------------------------------

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

def lca(root, p, q):
    if root == None:
        return None
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if root.data == p or root.data == q:
        return root.data
    elif left and right:
        return root.data
    return left or right

root = arrayToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(lca(root, 5, 1))
print(lca(root, 5, 4))
print(lca(root, 6, 5))

root = arrayToTree([1, 2])
print(lca(root, 1, 2))
