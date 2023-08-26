# DFS(Depth First Search) - 깊이 우선 탐색

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}
visited = []

def dfs(curr_v):
    visited.append(curr_v)

    for v in graph[curr_v]:
        if v not in visited:
            dfs(v)

dfs('A')
print(visited)
