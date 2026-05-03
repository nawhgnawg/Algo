from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dist = [[-2] * n for _ in range(n)]

q = deque()
for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            q.append((r, c))
            dist[r][c] = 0
        elif grid[r][c] == 0:
            dist[r][c] = -1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -2:
            if grid[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
            elif grid[nx][ny] == 2:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y]

for row in dist:
    print(*(row))

