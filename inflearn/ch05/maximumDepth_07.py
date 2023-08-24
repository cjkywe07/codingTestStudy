# Maximum Depth of Binary Tree(1)

'''
(1) 문제 이해
    0 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    postorder 이용 - O(n)

(3) 코드 설계
    base case

    left = maxDepth()
    right = maxDepth()

    return max(left, right) + 1

(4) 코드 구현
'''

# ------------------------------------------------------------

from arrayToTree_04 import arrayToTree

def maxDepth(root):
    if root == None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth, right_depth) + 1

root = arrayToTree([3, 9, 20, None, None, 15, 7])
print(maxDepth(root))

root = arrayToTree([1, None, 2])
print(maxDepth(root))

root = arrayToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(maxDepth(root))

root = arrayToTree([3, 5, 1, None, None, 0, 8])
print(maxDepth(root))
