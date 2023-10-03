# Number of Islands

'''
grid는 "1"(land)과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원배열이다.
이 지도에 표시된 섬들의 총 개수를 반환하시오.
섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러싸여있는 것을 말한다.
또한 grid의 네개의 가장자리는 모두 물로 둘러싸여있다고 가정하고 문제를 해결하라.

ex)
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
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
    m : 행의 개수 / n : 열의 개수
    1 <= m, n <= 300 에 따라 시간복잡도는 O(n^2) 이하의 알고리즘 사용
    300^2 -> 90000 -> 약 10^5

(2) 접근 방법
    bfs 이용
    bfs의 시간복잡도 -> O(방문하려는 정점의 개수) -> 약 O(m * n) -> 약 O(n^2)

(3) 코드 설계
    for i
        for j
            if grid[i][j] == 1 && not visited
                bfs

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque

# 01. visited를 list로
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
#                 if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
#                     if grid[next_r][next_c] == "1" and not visited[next_r][next_c]:
#                         visited[next_r][next_c] = True
#                         q.append((next_r, next_c))

#     for i in range(row):
#         for j in range(col):
#             if grid[i][j] == "1" and not visited[i][j]:
#                 bfs(i, j)
#                 islandCnt += 1

#     return islandCnt


# 02. visited를 set으로
def numIslands(grid):
    islandCnt = 0
    row = len(grid)
    col = len(grid[0])
    dr = [-1, 1, 0, 0]  # direction row (상하좌우)
    dc = [0, 0, -1, 1]  # direction colmun
    visited = set([])
    q = deque([])

    def bfs(r, c):  # r, c 는 행과 열의 인덱스
        visited.add((r, c))
        q.append((r, c))

        while q:
            cur_r, cur_c = q.popleft()

            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]

                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if grid[next_r][next_c] == "1" and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        q.append((next_r, next_c))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                islandCnt += 1

    return islandCnt


# 03. dfs로
# def numIslands(grid):
#     islandCnt = 0
#     row = len(grid)
#     col = len(grid[0])
#     dr = [-1, 1, 0, 0]  # direction row (상하좌우)
#     dc = [0, 0, -1, 1]  # direction colmun
#     visited = set([])

#     def dfs(r, c):  # r, c 는 행과 열의 인덱스
#         visited.add((r, c))

#         for i in range(4):
#             next_r = r + dr[i]
#             next_c = c + dc[i]
#             if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
#                 if grid[next_r][next_c] == "1" and (next_r, next_c) not in visited:
#                     visited.add((next_r, next_c))
#                     dfs(next_r, next_c)

#     for i in range(row):
#         for j in range(col):
#             if grid[i][j] == "1" and (i, j) not in visited:
#                 dfs(i, j)
#                 islandCnt += 1

#     return islandCnt


print(
    numIslands(
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

print(
    numIslands(
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
