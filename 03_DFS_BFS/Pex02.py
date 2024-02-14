# 프로그래머스 - 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 최단거리 -> BFS
maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]


# 1차 - BFS
def solution1(maps):
    answer = 0
    # N, M 구하기
    n = len(maps[0]) - 1
    m = len(maps) - 1
    leaves = [maps[0][0]]
    start = maps[0][0]
    temp = []
    # N x M이 갈 수 있는지
    if maps[n - 1][m] == 0 and maps[n][m - 1] == 0:
        return -1

    return answer


# 2차 - deque + Visited + BFS
from collections import deque
def solution2(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 있는 길인지 확인
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]

print(solution2(maps))