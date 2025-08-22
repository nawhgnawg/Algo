# 4179번 - 불!
# https://www.acmicpc.net/problem/4179
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(str, input()))[:-1] for _ in range(c)]

print(r, c)
print(graph)

def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for _ in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':    # 갈 수 있는 경우
                pass

queue = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            queue.append([i, j])    # J 위치 찾기

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            queue.append([i, j])    # F 위치 찾기

