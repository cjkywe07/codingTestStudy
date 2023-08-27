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

(2) 접근 방법
    bfs

(3) 코드 설계
    for i
        for j
            if grid[i][j] == 1 && not visited
                bfs

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque

def numIslands(grid):
    islandCnt = 0
    row = len(grid)
    col = len(grid[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * col for _ in range(row)]

    def bfs(r, c):
        visited[r][c] = True
        q = deque([(r, c)])

        while q:
            cur_r, cur_c = q.popleft()

            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if grid[next_r][next_c] == "1" and not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        q.append((next_r, next_c))
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                islandCnt += 1

    return islandCnt

numIslands(grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
