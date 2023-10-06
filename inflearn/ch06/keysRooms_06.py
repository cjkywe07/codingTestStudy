# Keys and Rooms

'''
0번 방부터 n - 1번 방까지 총 n개의 방이 있다.
0번 방을 제외한 모든 방은 잠겨있고, 목표는 모든 방에 방문하는 것이다.
하지만 잠겨있는 방은 key가 없으면 방문할 수 없다.
각 방에 방문할 때, 별개의 열쇠뭉치(a set of district keys)를 찾을 수도 있다.
각각의 열쇠에는 번호가 쓰여져 있고, 그 번호에 해당하는 방을 잠금 해제할 수 있다.
열쇠뭉치는 모두 가져갈 수 있고, 언제든 방 문을 열기 위해 사용할 수 있다.

문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
모든 방을 방문할 수 있다면 True, 그렇지 않다면 False를 반환하라.

ex)
    Input: rooms = [[1], [2], [3], []]
    Output: true

    Input: rooms = [[1, 3], [3, 0, 1], [2], [0]]
    Output: false

    Input: rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
    Output: false

제약조건
    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.
'''

# ------------------------------------------------------------

'''
(1) 문제 이해
    정점 개수(방의 개수) -> 최대 1000
    간선 개수(모든 방의 키의 개수의 합) -> 최대 3000

(2) 접근 방법
    bfs/dfs 이용

    bfs/dfs의 시간복잡도
    -> O(V + E) -> O(1000 + 3000) -> O(4 * 10^3)

(3) 코드 설계
    
(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque

'''(1) BFS'''
def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        visited[v] = True
        q = deque([v])

        while q:
            cur_v = q.popleft()

            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    q.append(next_v)

    bfs(0)

    return all(visited)


'''(2) DFS'''
# def canVisitAllRooms(rooms):
#     visited = [False] * len(rooms)

#     def dfs(v):
#         visited[v] = True

#         for next_v in rooms[v]:
#             if not visited[next_v]:
#                 dfs(next_v)

#     dfs(0)

#     return all(visited)


print(canVisitAllRooms(
    rooms = [[1], [2], [3], []]
))

print(canVisitAllRooms(
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
))

print(canVisitAllRooms(
    rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
))
