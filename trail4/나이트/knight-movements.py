from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

dist = [[-1] * n for _ in range(n)]

q = deque([(r1 - 1, c1 - 1)])
dist[r1 - 1][c1 - 1] = 0

while q:
    x, y = q.popleft()
    
    if x == r2 - 1 and y == c2 - 1:
        break
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

print(dist[r2 - 1][c2 - 1])