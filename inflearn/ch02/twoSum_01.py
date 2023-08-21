# Two Sum(1)

'''
정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target이
될수 있으면 True, 불가능하면 False를 반환하세요. 단, 같은 원소를 두 번 사용할 수 없습니다.

ex)
    Input: nums = {4, 1, 9, 7, 5, 3, 16} / target : 14
    Output: True

    Input: nums = {2, 1, 5, 7} / target : 4
    Output: False

제약조건
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    2 <= nums.length <= 10^4 에 따라 시간복잡도는 O(n^2) 보다 작은 알고리즘 사용

(2) 접근 방법
    보통 완전탐색으로 시작
    but, 이중반복문 - O(n^2) -> 실제로는 선택X, 연습만 해보기

(3) 코드 설계
    for i 0 ~ n
        for j i+1 ~ n
            if nums[i] + nums[j] == 14
                return True
    return False

(4) 코드 구현
'''

# ------------------------------------------------------------

def twoSum(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
            
    return False

print(twoSum([4, 1, 9, 7, 5, 3, 16], 14))
print(twoSum([2, 1, 5, 7], 4))
