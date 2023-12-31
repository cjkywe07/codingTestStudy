# Two Sum(2)

'''
(1) 문제 이해
    2 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    정렬 + two pointer 사용
    정렬 - O(nlogn) / two pointer - O(n)

(3) 코드 설계
    nums = [[n, i] for i, n in enumerate(nums)]
    nums.sort()
    l = 0
    r = n-1
    
    while l < r
        if nums[l][0] + nums[r][0] == target -> return [nums[l][1], nums[r][1]]
                                   <         -> l += 1
                                   >         -> r -= 1

    retrun None

(4) 코드 구현
'''

# ------------------------------------------------------------

# def twoSum(nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1

#     while l < r:
#         if nums[l] + nums[r] == target:
#             return True
#         elif nums[l] + nums[r] < target:
#             l += 1
#         elif nums[l] + nums[r] > target:
#             r -= 1
            
#     return False

def twoSum(nums, target):
    nums = [[n, i] for i, n in enumerate(nums)]
    # nums.sort(key = lambda x: x[0])
    nums.sort()
    l, r = 0, len(nums) - 1

    while l < r:
        sum = nums[l][0] + nums[r][0]

        if sum == target:
            return [nums[l][1], nums[r][1]]
        elif sum < target:
            l += 1
        else:
            r -= 1

    return None

print(twoSum([4, 1, 9, 7, 5, 3, 16], 14))
print(twoSum([2, 1, 5, 7], 4))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
