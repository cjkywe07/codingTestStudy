# Unique Paths

'''
이 로봇은 m x n grid(격자) 위에 있습니다.
로봇은 처음에 좌측 상단 모서리 (grid[0][0])에 위치에 있습니다.
로봇은 우측 하단 모서리 (grid[m - 1][n - 1])로 이동하려고 합니다.
로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있습니다.
두 정수 m과 n이 주어졌을 때, 로봇이 우측 하단 모서리에 도달할 수 있는 가능한 unique paths의 수를 반환하세요.
단, 테스트 케이스는 답이 2 * 10^9 이하가 되도록 생성합니다.

ex)
    Input: m = 3, n = 7
    Output: 28

    Input: m = 3, n = 2
    Output: 3

제약조건
    1 <= m, n <= 100
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    테스트 케이스(output)의 값이 2 * 10^9 이하가 된다는 것은
    (1) 2 * 10^9 -> 약 2^31 이므로,
        -2^31 ~ 2^31 + 1 까지 표현 가능한 int 자료형 사용해도 된다는 의미
    (2) 실행 횟수가 최대 2 * 10^9 까지 될 수도 있으므로,
        완전탐색 사용 시 시간초과 난다는 의미

    DP 사용 시 반복 계산 줄여
    O(m * n) -> O(10000) -> O(10^4) 으로 해결 가능

(2) 접근 방법
    (0, 0) 에서 (m - 1, n - 1) 까지 가는 방법수
    -> (m - 2, n - 1) 까지 가는 방법수 + (m - 1, n - 2) 까지 가는 방법수
       [위쪽과 왼쪽에서 올 수 있으므로]
    
    ex) (0, 0) 에서 (2, 6) 까지 가는 방법수
        -> (1, 6) 까지 가는 방법수 + (2, 5) 까지 가는 방법수

    base case
    1) (0, 0)까지 가는 방법수 -> 1
    2) (0, x) or (x, 0)까지 가는 방법수 -> 모두 1

    DP 이용

(3) 코드 설계
    1) 완전탐색
        # r : m - 1 / c : n - 1
        def dp(r, c):
            unique_paths = 0

            if r == 0 and c == 0:
                return 1
            
            if r - 1 >= 0:
                unique_paths += dp(r - 1, c)

            if c - 1 >= 0:
                unique_paths += dp(r, c - 1)
            
            return unique_paths

        --------------------------------------

        def dp(r, c):
            unique_paths = 0

            if r == 0 or c == 0:
                return 1
            
            unique_paths += dp(r - 1, c)
            unique_paths += dp(r, c - 1)
            
            return unique_paths

    2) Top-down
    3) Bottom-up

(4) 코드 구현
'''

# ------------------------------------------------------------

# uniquePaths

'''(1) Top-down'''
# (1)
# def up_1(m, n):
#     memo = [[-1] * n for _ in range(m)]
    
#     def dp(r, c):
#         unique_paths = 0

#         if r == 0 and c == 0:
#             memo[r][c] = 1
        
#         if memo[r][c] == -1:
#             if r - 1 >= 0:
#                 unique_paths += dp(r - 1, c)

#             if c - 1 >= 0:
#                 unique_paths += dp(r, c - 1)

#             memo[r][c] = unique_paths

#         return memo[r][c]
            
#     return dp(m - 1, n - 1)

# (2)
def up_1(m, n):
    memo = [[-1] * n for _ in range(m)]
    
    def dp(r, c):
        unique_paths = 0

        if memo[r][c] == -1:
            if r == 0 or c == 0:
                memo[r][c] = 1
                return memo[r][c]
            
            unique_paths += dp(r - 1, c)
            unique_paths += dp(r, c - 1)

            memo[r][c] = unique_paths

        return memo[r][c]
            
    return dp(m - 1, n - 1)


'''(2) Bottom-up'''
def up_2(m, n):
    memo = [[-1] * n for _ in range(m)]
    
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1
    
    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r - 1][c] + memo[r][c - 1]

    return memo[m - 1][n - 1]


print(up_1(m = 3, n = 7))
print(up_2(m = 3, n = 7))
