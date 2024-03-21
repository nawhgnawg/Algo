# 프로그래머스 - 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

# 1차 - BFS (index range 오류)
from collections import deque
def solution1(maps):
    answer = 0
    m, n = len(maps), len(maps[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    L = False
    q = deque()

    # 시작 찾기
    for x in range(m):
        for y in range(n):
            if maps[x][y] == "S":
                sx, sy = x, y
    q.append((sx, sy, L, 0))

    while q:
        x, y, l, level = q.popleft()

        # "E"를 만나고 L가 True일 때
        if maps[x][y] == "E" and L:
            answer = level
            break

        for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == "X":
                    if maps[nx][ny] == "L":
                        l = True
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, l, level + 1))
    return answer

# 2차 - BFS
# 출발 지점에서 레버로, 레버에서 출구로 BFS알고리즘을 2번 수행하면 된다!
from collections import deque
def bfs(start, end, maps):
    # 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]

    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False

    # 초기값 설정
    for i in range(n):
        for j in range(m):
            # 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    # BFS 알고리즘 수행
    while q:
        y, x, cost = q.popleft()
        if maps[y][x] == end:
            return cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if ny >= 0 and ny < n and nx >= 0 and nx < m and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, cost + 1))
                    visited[ny][nx] = True

    return -1   # 탈출할 수 없다면

def solution2(maps):
    path1 = bfs('S', 'L', maps)     # 시작 지점 -> 레버
    path2 = bfs('L', 'E', maps)     # 레버 -> 출구

    # 둘다 -1이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2

    # 둘중 하나라도 -1이면 탈출할 수 없음
    return -1


print(solution2(maps))