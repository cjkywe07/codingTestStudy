# Two Sum(3)

'''
ch02 List 의 Two Sum 문제

(1) 문제 이해
    2 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    해시테이블 사용
    (리스트와는 달리 in 연산자를 통해 특정 key값이 존재하는지 O(1)의 시간복잡도로 확인 가능)

(3) 코드 설계
    for v in nums
        dict[n] = 1

    for v in nums
        n = target - v
        if n != v && n in dict
            return T

    return F

(4) 코드 구현
'''

# ------------------------------------------------------------

# def twoSum(nums, target):
#     memo = {}

#     for v in nums:
#         memo[v] = 1

#     for v in nums:
#         needed_num = target - v
#         if needed_num != v and (needed_num in memo):
#             return True
        
#     return False

def twoSum(nums, target):
    memo = {}

    for i, v in enumerate(nums):
        if v in memo:
            memo[v].append(i)
        else:
            memo[v] = [i]

    for v in nums:
        needed_num = target - v

        if needed_num in memo:
            if v == needed_num:
                if len(memo[v]) >= 2:
                    return[memo[v][0], memo[v][1]]
            else:
                return [memo[v][0], memo[needed_num][0]]
        
    return []

print(twoSum([4, 1, 9, 7, 5, 3, 16], 14))
print(twoSum([2, 1, 5, 7], 4))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
