# Dijkstra

import heapq

graph1 = {
    # (비용, 정점번호)
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}

graph2 = {
    0: [(1, 1), (2, 3)],
    1: [(4, 2), (3, 3), (1, 4), (6, 5)],
    2: [(1, 5), (1, 6), (2, 7)],
    3: [(5, 4)],
    4: [(2, 6)],
    5: [],
    6: [(1, 7)],
    7: []
}

def dijkstra(graph, start, end):
    costs = {}
    prev = [None] * (len(graph) + 1)
    path = []
    pq = []
    heapq.heappush(pq, (0, start, start))
    # (현재비용, 현재정점, 이전정점)
    # 첫 번째 정점은 이전 정점이 없으므로 그냥 해당 정점을 이전 정점으로 넣어줌
    
    # 최소 비용 기록하는 costs 딕셔너리와
    # 직전 정점 기록하는 prev 리스트 생성
    while pq:
        cur_cost, cur_v, prev_v = heapq.heappop(pq)

        if cur_v not in costs:
            costs[cur_v] = cur_cost

            if prev[cur_v] == None:
                prev[cur_v] = prev_v

            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v, cur_v))

    # 최단거리 경로 나타내는 path 리스트 생성
    path.append(end)
    back = end
    while back != start:
        path.append(prev[back])
        back = prev[back]
    path.reverse()

    # return path  # 최단 경로 반환
    # return costs[end]  # 최소 비용 반환
    return [path, costs[end]]

# s -> e 까지 가는 최소 비용 / 최단 경로
print(dijkstra(graph1, 1, 8))
print(dijkstra(graph2, 0, 7))
