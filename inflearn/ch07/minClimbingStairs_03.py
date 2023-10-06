# Min Cost Climbing Stairs

'''
계단을 올라가고 있다. 한 번 올라갈 때마다 1 step 또는 2 steps 올라갈 수 있다.
문제에서 정수형 배열 cost가 주어지는데,
cost[i]는 i번 째 계단을 밟고 1step/2step 이동할 때 지불해야 하는 비용이다.
처음 시작은 index 0 또는 index 1 중 한 곳에서 시작할 수 있다.
이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소값을 반환하라.

ex)
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation:
        You will start at index 1.
        Pay 15 and climb two steps to reach the top.
        The total cost is 15.

    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6

    Input: cost = [10, 15, 20, 17, 1]
    Output: 31

제약조건
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    2 <= cost.length <= 10^3 에 따라 O(n^2) 이하의 알고리즘 사용

(2) 접근 방법
    특정 층까지 올라가는 최소 비용
    -> (해당 층 - 1 층까지 올라가는 최소비용 + 해당 층 - 1 층의 비용) 과
       (해당 층 - 2 층까지 올라가는 최소비용 + 해당 층 - 2 층의 비용) 중 더 작은 값

    base case
    0, 1층에서 시작할 수 있으므로
    0, 1층까지 올라가는 최소 비용 -> 0

    DP 이용

(3) 코드 설계
    1) 재귀
        def mcs(n):
            if n == 0 or n == 1:
                return 0

            return min(mcs(n - 1) + cost[n - 1], mcs(n - 2) + cost[n - 2])

    2) Top-down
    3) Bottom-up

(4) 코드 구현
'''

# ------------------------------------------------------------

# minCostClimbingStairs

'''(1) Top-down'''
def mccs_1(cost):
    memo = {}
    n = len(cost)

    def dp(n):
        if n == 0 or n == 1:
            return 0
        
        if n not in memo:
            memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])

        return memo[n]

    return dp(n)


'''(2) Bottom-up'''
def mccs_2(cost):
    memo = {0: 0, 1: 0}
    n = len(cost)

    # memo = [-1] * (n + 1)
    # memo[0] = 0
    # memo[1] = 0

    for i in range(2, n + 1):
        memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])

    return memo[n]


print(mccs_1(
    cost = [10, 15, 20, 17, 1]
))

print(mccs_2(
    cost = [10, 15, 20, 17, 1]
))
