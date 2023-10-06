# 암시적 그래프(implicit graph)

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
row_len = len(grid)
col_len = len(grid[0])


'''BFS'''
# (1)
from collections import deque

def isValid(r, c):
    return (0 <= r < row_len) and (0 <= c < col_len) and (grid[r][c] == 1)

def bfs(grid, r, c):
    row_len = len(grid)
    col_len = len(grid[0])

    visited = [[False] * col_len for _ in range(row_len)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append(r, c)
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            # if (next_r >= 0 and next_r < row_len) and (next_c >= 0 and next_c < col_len):
            #     if grid[next_r][next_c] == 1:
            #         if not visited[next_r][next_c]:
            #             queue.append((next_r, next_c))
            #             visited[next_r][next_c] = True

            if isValid(next_r, next_c):
                if not visited[next_r][next_c]:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True

bfs(grid, 0, 0)


# (2)
def bfs(grid):
    def isValid(r, c):
        return (
            (r >= 0 and r < row_len)
            and (c >= 0 and c < col_len)
            and grid[r][c] == 1
        )
    
    row_len, col_len = len(grid), len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]
    dr = [0,  1,  1,  1,  0, -1, -1, -1]
    dc = [1,  1,  0, -1, -1, -1,  0,  1]

    queue = deque()
    queue.append(0, 0)
    visited[0][0] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(8):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if isValid(next_r, next_c):
                if not visited[next_r][next_c]:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True

bfs(grid)

# ------------------------------------------------------------

'''DFS'''
# (1)
def dfs(r, c):
    visited[r][c] = True

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if (0 <= next_r < row_len) and (0 <= next_c < col_len):
            if grid[next_r][next_c] == 1:
                if not visited[next_r][next_c]:
                    dfs(next_r, next_c)

row_len, col_len = len(grid), len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
dfs(0, 0)


# (2)
def isValid(r, c):
    return (0 <= r < row_len) and (0 <= c < col_len) and (grid[r][c] == 1)

def dfs(r, c):
    visited[r][c] = True

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if isValid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)

row_len, col_len = len(grid), len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dfs(0, 0)

# ------------------------------------------------------------

'''정리'''

# 행과 열이 유효한 idx 범위에 존재하고,
# grid[r][c] 가 지나갈 수 있는 정점이라면(아래 예시에서는 1인 경우)
# True 반환
def isValid(r, c):
    return(
        (0 <= r < row_len) and
        (0 <= c < col_len) and
        (grid[r][c] == 1)
    )

grid = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
]

row_len = len(grid)
col_len = len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
# directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


'''BFS'''
def dfs(r, c):
    visited[r][c] = True
    q = deque()
    q.append((r, c))
    
    while q:
        cur_r, cur_c = q.popleft()
        
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if isValid(next_r, next_c):
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))

bfs(0, 0)


'''DFS'''
def dfs(r, c):
    visited[r][c] = True

    for dr, dc in directions:
        next_r = r + dr
        next_c = c + dc

        if isValid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)

dfs(0, 0)
