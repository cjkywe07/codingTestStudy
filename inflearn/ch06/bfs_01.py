# BFS(Breadth First Search) - 너비 우선 탐색

from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

def bfs(graph, start_v):
    visited = [start_v]
    q = deque(start_v)
    
    while q:
        curr_v = q.popleft()
        for v in graph[curr_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    
    return visited

print(bfs(graph, 'A'))
