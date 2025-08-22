# 7576번 - 토마토
# https://www.acmicpc.net/problem/7576

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

# 익은 토마토 위치 queue에 추가
queue = deque()
for i in range(m):
    for j in range(n):
        if data[i][j] == 1:
            queue.append([i, j])

# BFS
def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:   # 안 익은 토마토 찾기
                data[nx][ny] = data[x][y] + 1   # 몇 번째인지 체크 하기위해 + 1
                queue.append([nx, ny])          # 안익은 토마토 queue에 넣기

# 토마토 익히기 시작
bfs()

day = 0
for row in data:
    for i in row:
        if i == 0:  # 안 익은 토마토가 있으면 return -1
            print(-1)
            exit()
        else:       # 다 익었으면 max 비교
            day = max(day, max(row))
print(day - 1)

# 9 8 7 6 5 4
# 8 7 6 5 4 3
# 7 6 5 4 3 2
# 6 5 4 3 2 1