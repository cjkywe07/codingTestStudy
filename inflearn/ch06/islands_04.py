# Number of Islands

'''
grid는 "1"(land)과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원배열이다.
이 지도에 표시된 섬들의 총 개수를 반환하시오.
섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러싸여있는 것을 말한다.
또한 grid의 네개의 가장자리는 모두 물로 둘러싸여있다고 가정하고 문제를 해결하라.

ex)
    Input: grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    Output: 1

    Input: grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    Output: 3

제약조건
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    정점 개수 V -> 행길이 * 열길이 -> 최대 90000

(2) 접근 방법
    bfs/dfs 이용

    bfs/dfs의 시간복잡도
    -> O(V)
    -> O(90000) -> 약 O(10^5)

(3) 코드 설계
    for i
        for j
            if grid[i][j] == 1 && not visited
                bfs

(4) 코드 구현
'''

# ------------------------------------------------------------

# from collections import deque

'''(1) BFS / visited - list'''
# def numIslands(grid):
#     islandCnt = 0
#     row = len(grid)
#     col = len(grid[0])
#     dr = [-1, 1, 0, 0]  # direction row (상하좌우)
#     dc = [0, 0, -1, 1]  # direction colmun
#     visited = [[False] * col for _ in range(row)]

#     def bfs(r, c):  # r, c 는 행과 열의 인덱스
#         visited[r][c] = True
#         q = deque([(r, c)])

#         while q:
#             cur_r, cur_c = q.popleft()

#             for i in range(4):
#                 next_r = cur_r + dr[i]
#                 next_c = cur_c + dc[i]

#                 if (next_r >= 0 and next_r < row) and (next_c >= 0 and next_c < col):
#                     if (grid[next_r][next_c] == "1") and (not visited[next_r][next_c]):
#                         visited[next_r][next_c] = True
#                         q.append((next_r, next_c))

#     for i in range(row):
#         for j in range(col):
#             if (grid[i][j] == "1") and (not visited[i][j]):
#                 bfs(i, j)
#                 islandCnt += 1

#     return islandCnt


'''(2) BFS / visited - set'''
# def numIslands(grid):
#     islandCnt = 0
#     row = len(grid)
#     col = len(grid[0])
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     visited = set()
#     q = deque()

#     def bfs(r, c):
#         visited.add((r, c))
#         q.append((r, c))

#         while q:
#             cur_r, cur_c = q.popleft()

#             for i in range(4):
#                 next_r = cur_r + dr[i]
#                 next_c = cur_c + dc[i]

#                 if (next_r >= 0 and next_r < row) and (next_c >= 0 and next_c < col):
#                     if (grid[next_r][next_c] == "1") and ((next_r, next_c) not in visited):
#                         visited.add((next_r, next_c))
#                         q.append((next_r, next_c))

#     for i in range(row):
#         for j in range(col):
#             if (grid[i][j] == "1") and ((i, j) not in visited):
#                 bfs(i, j)
#                 islandCnt += 1

#     return islandCnt


'''(3) DFS'''
# def numIslands(grid):
#     islandCnt = 0
#     row = len(grid)
#     col = len(grid[0])
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     visited = set()

#     def dfs(r, c):
#         visited.add((r, c))

#         for i in range(4):
#             next_r = r + dr[i]
#             next_c = c + dc[i]

#             if (next_r >= 0 and next_r < row) and (next_c >= 0 and next_c < col):
#                 if (grid[next_r][next_c] == "1") and ((next_r, next_c) not in visited):
#                     visited.add((next_r, next_c))
#                     dfs(next_r, next_c)

#     for i in range(row):
#         for j in range(col):
#             if (grid[i][j] == "1") and ((i, j) not in visited):
#                 dfs(i, j)
#                 islandCnt += 1

#     return islandCnt

# ------------------------------------------------------------

'''정리'''

'''(1) BFS'''
from collections import deque

def numIslands(grid):
    islands_cnt = 0
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def isValid(r, c):
        return (
            (r >= 0 and r < row_len) and
            (c >= 0 and c < col_len) and
            (grid[r][c] == "1")
        )

    def bfs(r, c):
        visited[r][c] = True
        q = deque([(r, c)])

        while q:
            cur_r, cur_c = q.popleft()

            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if isValid(next_r, next_c):
                    if not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        q.append((next_r, next_c))

    for i in range(row_len):
        for j in range(col_len):
            if (grid[i][j] == "1") and (not visited[i][j]):
                bfs(i, j)
                islands_cnt += 1

    return islands_cnt


'''(1) DFS'''
# def numIslands(grid):
#     islands_cnt = 0
#     row_len = len(grid)
#     col_len = len(grid[0])
#     visited = [[False] * col_len for _ in range(row_len)]
#     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

#     def isValid(r, c):
#         return (
#             (r >= 0 and r < row_len) and
#             (c >= 0 and c < col_len) and
#             (grid[r][c] == "1")
#         )

#     def dfs(r, c):
#         visited[r][c] = True

#         for dr, dc in directions:
#             next_r = r + dr
#             next_c = c + dc

#             if isValid(next_r, next_c):
#                 if not visited[next_r][next_c]:
#                     visited[next_r][next_c] = True
#                     dfs(next_r, next_c)

#     for i in range(row_len):
#         for j in range(col_len):
#             if (grid[i][j] == "1") and (not visited[i][j]):
#                 dfs(i, j)
#                 islands_cnt += 1

#     return islands_cnt


print(
    numIslands(
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    )
)

print(
    numIslands(
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    )
)
