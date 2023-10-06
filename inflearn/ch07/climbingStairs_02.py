# Climbing Stairs

'''
계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다.
한 번 올라갈 때마다 1 step 또는 2 steps 올라갈 수 있다.
꼭대기에 도달하는 방법의 개수는 총 몇 가지인가?

ex)
    Input: n = 2
    Output: 2
        1. 1 step + 1 step
        2. 2 steps

    Input: n = 3
    Output: 3
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

제약조건
    1 <= n <= 45
'''

# ------------------------------------------------------------

'''
(1) 문제 이해

(2) 접근 방법
    특정 층까지 올라가는 방법의 개수
    -> (해당 층 - 1 층까지 올라가는 방법수) + (해당 층 - 2 층까지 올라가는 방법수)

    base case
    1층까지 올라가는 방법수 -> 1가지
    2층까지 올라가는 방법수 -> 2가지

    DP 이용

(3) 코드 설계
    1) 재귀
        def cs(n):
            if n == 1: return 1
            if n == 2: return 2

            return cs(n - 1) + cs(n - 2)

    2) Top-down
    3) Bottom-up

(4) 코드 구현
'''

# ------------------------------------------------------------

# climbStairs

'''(1) Top-down'''
# (1)
# memo_1 = {}

# def cs_1(n):
#     if n == 1: return 1
#     if n == 2: return 2
    
#     if n not in memo_1:
#         memo_1[n] = cs_1(n - 1) + cs_1(n - 2)

#     return memo_1[n]

# (2)
def cs_1(n):
    memo = {}

    def dp(n):
        if n == 1: return 1
        if n == 2: return 2
            
        if n not in memo:
            memo[n] = dp(n - 1) + dp(n - 2)

        return memo[n]

    return dp(n)


'''(2) Bottom-up'''
# (1)
# memo_2 = {1: 1, 2: 2}

# def cs_2(n):
#     for i in range(3, n + 1):
#         memo_2[i] = memo_2[i - 1] + memo_2[i - 2]

#     return memo_2[n]

# (2)
def cs_2(n):
    memo = {1: 1, 2: 2}

    def dp(n):
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

    return dp(n)


print(cs_1(5))
print(cs_2(5))
