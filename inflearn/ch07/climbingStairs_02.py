# Climbing stairs

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
    특정 층까지 올라가는 방법의 개수는
    (해당 층 - 1 층까지 올라가는 방법수) + (해당 층 - 2 층까지 올라가는 방법수)

    DP 이용

(3) 코드 설계
    1) 재귀
        def cs(n)
            if n == 1 return 1
            if n == 2 return 2

            return cs(n-1) + cs(n-2)

    2) Top-down
    3) Bottom-up

(4) 코드 구현
'''

# ------------------------------------------------------------

# (1) Top-down
memo = {}

def cs_1(n):
    if n == 1: return 1
    
    if n == 2: return 2
    
    if n not in memo:
        memo[n] = cs_1(n - 1) + cs_1(n - 2)

    return memo[n]


# (2) Bottom-up
memo = {1: 1, 2: 2}

def cs_2(n):
    for i in range(3, n + 1):
        memo[n] = memo[i - 1] + memo[i - 2]

    return memo[n]


print(cs_1(5))
print(cs_2(5))
