# Maximum Depth of Binary Tree(1)

'''
문제에서 binary tree 하나가 주어진다. 주어진 binary tree의 최대 깊이를 반환해라.

ex)
    Input: root = [3, 9, 20, None, None, 15, 7]
    Output: 3

    Input: root = [1, None, 2]
    Output: 2

제약조건
    0 <= node의 개수 <= 10^4
    -100 <= Node.val <= 100
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    0 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    level order 이용 - O(n)

(3) 코드 설계
    q = deque()
    q.append(root)
    
    while q:
        curr = q.popleft()
        q.append((leftRight, depth))

    return maxDepth

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque
from arrayToTree_04 import arrayToTree

def maxDepth(root):
    if root == None:
        return max_depth
    
    max_depth = 0
    q = deque()
    q.append((root, 1))

    while q:
        curr_node, curr_depth = q.popleft()
        max_depth = max(max_depth, curr_depth)

        if curr_node.left:
            q.append((curr_node.left, curr_depth + 1))
        if curr_node.right:
            q.append((curr_node.right, curr_depth + 1))

    return max_depth

root = arrayToTree([3, 9, 20, None, None, 15, 7])
print(maxDepth(root))

root = arrayToTree([1, None, 2])
print(maxDepth(root))

root = arrayToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(maxDepth(root))

root = arrayToTree([3, 5, 1, None, None, 0, 8])
print(maxDepth(root))
