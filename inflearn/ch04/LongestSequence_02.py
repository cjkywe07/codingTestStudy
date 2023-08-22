# Longest Consecutive Sequence(1)

'''
정렬되어 있지 않은 정수형 배열 nums가 주어졌다.
nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 개수는 몇개인지 반환하시오.

ex)
    Input: nums = [100,4,200,1,3,2]
    Output: 4 (가장 긴 연속된 수: [1,2,3,4])

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9 (가장 긴 연속된 수: [0,1,2,3,4,5,6,7,8])
 

제약조건
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    0 <= nums.length <= 10^5 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    해시테이블 사용

(3) 코드 설계
    for n in nums
        numsDict[n] = 1

    for n in nums
        if prevNum not in numsDict
            cnt = 1
            while nextNum in numsDict
                cnt += 1
                nextNum += 1
    
    return longCnt

(4) 코드 구현
'''

# ------------------------------------------------------------

'''딕셔너리 이용'''
# def longestConsecutive(nums):
#     longestCnt = 0
#     numDict = {}

#     for num in nums:
#         numDict[num] = 1

#     for num in numDict:
#         if num - 1 not in numDict:
#             cnt = 1
#             nextNum = num + 1
            
#             while nextNum in numDict:
#                 cnt += 1
#                 nextNum += 1
            
#             longestCnt = max(longestCnt, cnt)

#     return longestCnt

'''셋 이용'''
def longestConsecutive(nums):
    longestCnt = 0
    numSet = set(nums)

    for num in numSet:
        if num - 1 not in numSet:
            cnt = 1
            nextNum = num + 1
            
            while nextNum in numSet:
                cnt += 1
                nextNum += 1
            
            longestCnt = max(longestCnt, cnt)

    return longestCnt

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([]))
