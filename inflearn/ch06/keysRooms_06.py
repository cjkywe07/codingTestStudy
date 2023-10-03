# Keys and Rooms

'''
0번 방부터 n - 1번 방까지 총 n개의 방이 있다.
0번 방을 제외한 모든 방은 잠겨있고, 목표는 모든 방에 visit하는것이다.
하지만 잠겨있는 방은 key가 없으면 visit할 수 없다.
각 방에 방문할 때, 별개의 열쇠뭉치(a set of distict keys)를 찾을 수도 있다.
각각의 열쇠에는 number가 쓰여져 있고, 그 번호에 해당하는 방을 잠금 해제할 수 있다.
열쇠뭉치는 모두 가져갈 수 있고, 언제든 방 문을 열기 위해 사용할 수 잇다.

문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
모든 방을 visit할 수 있다면 True, 그렇지 않다면 False를 반환하라.

ex)
    Input: rooms = [[1],[2],[3],[]]
    Output: true

    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false

    Input: 
    Output: 

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
    2 <= 방의 개수(정점의 개수) <= 1000 / 2 <= n <= 10^3 에 따라 O(n^2) 이하의 알고리즘 사용
    0 <= 한 방에 있을 수 있는 키의 개수 <= 1000
    1 <= 모든 방의 키의 개수의 합(간선의 개수) <= 3000

    bfs/dfs 를 사용한다면 O(V + E) -> O(1000 + 3000) -> O(4 * 10^3)

(2) 접근 방법
    bfs/dfs 이용

(3) 코드 설계
    

(4) 코드 구현
'''

# ------------------------------------------------------------

from collections import deque

''' dfs '''
# def canVisitAllRooms(rooms):
#     visited = [False] * len(rooms)

#     def dfs(v):
#         visited[v] = True

#         for next_v in rooms[v]:
#             if visited[next_v] == False:
#                 dfs(next_v)

#     dfs(0)

#     return all(visited)


''' bfs '''
def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        visited[v] = True
        q = deque([v])

        while q:
            cur_v = q.popleft()

            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    visited[next_v] = True
                    q.append(next_v)

    bfs(0)

    return all(visited)


print(canVisitAllRooms(
    rooms = [[1], [2], [3], []]
))

print(canVisitAllRooms(
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
))

print(canVisitAllRooms(
    rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
))
