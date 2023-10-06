# BFS(Breadth First Search) - 너비 우선 탐색

from collections import deque

# 인접 리스트
# graph = {
#     'A': ['B', 'D', 'E'],
#     'B': ['A', 'C', 'D'],
#     'C': ['B'],
#     'D': ['A', 'B'],
#     'E': ['A']
# }

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5]
}


''' visited를 list로 '''
# def bfs(graph, start_v):
#     visited = [start_v]
#     q = deque([start_v])
    
#     while q:
#         cur_v = q.popleft()

#         for next_v in graph[cur_v]:
#             if next_v not in visited:
#                 visited.append(next_v)
#                 q.append(next_v)
    
#     return visited


''' visited를 dictionary로 '''
def bfs(graph, start_v):
    visited = {start_v: True}
    q = deque([start_v])
    
    while q:
        cur_v = q.popleft()

        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited[next_v] = True
                q.append(next_v)
    
    return list(visited.keys())


''' visited를 set으로 '''
''' 방문 순서 중요하므로 set은 사용 X '''

print(bfs(graph, 0))
