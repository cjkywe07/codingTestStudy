# Shortest Path in Binary Matrix

'''
n x n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는
가장 빠른 경로의 길이를 반환하시오. 만약 경로가 없다면 -1을 반환하시오.

출발지 : top-left cell
목적지 : bottom-right cell

- 값이 0인 cell만 지나갈 수 있다.
- cell끼리는 8가지 방향으로 연결되어 있다. (edge와 corner 방향으로 총 8가지)
- 연결된 cell을 통해서만 지나갈 수 있다.

ex)
    Input: grid = [
        [0,1],
        [1,0]
    ]
    Output: 2

    Input: grid = [
        [0,0,0],
        [1,1,0],
        [1,1,0]
    ]
    Output: 4

    Input: grid = [
        [1,0,0],
        [1,1,0],
        [1,1,0]
    ]
    Output: -1

제약조건
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    1 <= n <= 100 에 따라 O(n^2) 이하의 알고리즘 사용
    100^2 -> 10000 -> 10^4

(2) 접근 방법
    bfs 이용

    dfs로 탐색한다면 모든 경우의 수를 다 비교해봐야 함
    bfs로 탐색한다면 가까운 곳부터 순차적으로 접근하다 목적지에 도착하면 그것이 최단경로 -> 보다 적합

(3) 코드 설계
    

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0 or grid[row - 1][col - 1] != 0:
        return shortest_path_len

    # visited = [[False] * col for _ in range(row)]
    visited = set([])

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # visited[0][0] = True
    visited.add((0, 0))
    q = deque([(0, 0, 1)])

    while q:
        cur_r, cur_c, cur_len = q.popleft()

        if cur_r == row - 1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break

        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if grid[next_r][next_c] == 0 and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    q.append((next_r, next_c, cur_len + 1))

    return shortest_path_len

print(
    shortestPathBinaryMatrix(
        grid = [
            [0, 1],
            [1, 0]
        ]
    )
)

print(
    shortestPathBinaryMatrix(
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
    )
)

print(
    shortestPathBinaryMatrix(
        grid = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
    )
)
