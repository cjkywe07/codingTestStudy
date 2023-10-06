# Network Delay Time

'''
주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블이 붙어있습니다.
또한 times[i] = (ui, vi, wi) 리스트가 주어집니다.
이때, ui 노드에서 신호를 보내서 vi 노드에 도달하는데 걸리는 시간을 wi 라고 합니다.

k 노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오.
하나의 노드라도 도달하지 못한다면 -1을 반환하시오.
(한 노드에서 연결된 여러 개의 edge에 신호를 동시에 전달할 수 있습니다.)

ex)
    Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
    Output: 2

    Input: times = [[1, 2, 1]], n = 2, k = 1
    Output: 1

    Input: times = [[1, 2, 1]], n = 2, k = 2
    Output: -1

    Input: times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]], n = 4, k = 2
    Output: 4

    Input: times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]], n = 4, k = 3
    Output: -1

제약조건
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    모든 (ui, vi) 쌍은 unique 합니다 (i.e., no multiple edges.)
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    1 <= 시작 노드 <= 노드 개수 <= 100
    1 <= 간선 개수 <= 6000
    1 <= 연결된 두 개의 노드 <= n
    연결된 두 개의 노드는 서로 다른 숫자
    0 <= 비용(가중치) <= 100
    두 노드를 연결하는 간선 수는 하나

(2) 접근 방법
    가중치를 이용하여 최소 비용을 구하는 문제이므로 다익스트라 이용

(3) 코드 설계
    그래프 구현
        O(간선 개수) -> O(6000) -> O(10^4) 미만
    
    다익스트라 알고리즘
        heappush/heappop이 O(logE) 이고, 간선의 개수만큼 일어날 수 있으므로,
        O(ElogE) -> O(6000 * log6000) -> O( 6000 * 약 log(8*(2^10)) ) -> O(6000 * 13) -> O(10^5) 미만

    방문 못한 노드 찾기
        O(n)

    최소비용 중에서 최댓값 찾기
        O(n)

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import defaultdict
import heapq

def networkDelayTime(times, n, k):
    # 그래프 구현
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((w, v))

    # 다익스트라 알고리즘
    costs = {}
    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)

        if cur_v not in costs:
            costs[cur_v] = cur_cost

            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    # 방문 못한 노드 찾기
    for v in range(1, n + 1):
        if v not in costs:
            return -1

    # 최소비용 중에서 최댓값 찾기
    return max(costs.values())

print(
    networkDelayTime(
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
        n = 4,
        k = 2
    )
)

print(
    networkDelayTime(
        times = [[1, 2, 1]],
        n = 2,
        k = 2
    )
)

print(
    networkDelayTime(
        times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]],
        n = 4,
        k = 2
    )
)
