# Longest Consecutive Sequence(2)

'''
(1) 문제 이해
    0 <= nums.length <= 10^5 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    정렬[O(nlogn)] 후 연속된 수 탐색[O(n)]

(3) 코드 설계
    nums.sort()
    cnt = 1

    for i in range(len - 1)
        if nums[i] + 1 == nums[i + 1]
            cnt += 1
        else
            cnt = 1

    return longCnt

(4) 코드 구현
'''

# ------------------------------------------------------------

def longestConsecutive(nums):
    if not len(nums): return 0

    nums.sort()
    longestCnt = 0
    cnt = 1

    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            cnt += 1
        else:
            longestCnt = max(longestCnt, cnt)
            cnt = 1

    longestCnt = max(longestCnt, cnt)
    return longestCnt

print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([11, 3, 9, 2, 10, 1, 12]))
print(longestConsecutive([7, 3, 9, 2, 11, 1, 12]))
print(longestConsecutive([]))
