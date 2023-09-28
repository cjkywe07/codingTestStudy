# DFS(Depth First Search) - 깊이 우선 탐색

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
# visited = []

# def dfs(cur_v):
#     visited.append(cur_v)

#     for next_v in graph[cur_v]:
#         if next_v not in visited:
#             dfs(next_v)

''' visited를 dictionary로 '''
visited = {}

def dfs(cur_v):
    visited[cur_v] = True

    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)

dfs(0)
print(visited)
