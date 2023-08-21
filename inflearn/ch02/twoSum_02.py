# Two Sum(2)

'''
(1) 문제 이해
    2 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    정렬, two pointer 사용
    정렬 - O(nlogn) / two pointer - O(n)

(3) 코드 설계
    nums.sort()
    l = 0
    r = n-1
    
    while l < r
        if nums[l] + nums[r] == target -> return True
                             <         -> l += 1
                             >         -> r -= 1
    retrun False

(4) 코드 구현
'''

# ------------------------------------------------------------

def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
            
    return False

print(twoSum([4, 1, 9, 7, 5, 3, 16], 14))
print(twoSum([2, 1, 5, 7], 4))
