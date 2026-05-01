from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dist = [[-1] * m for _ in range(n)]

q = deque([(0, 0)])
dist[0][0] = 0

while q:
    x, y = q.popleft()

    if x == n - 1 and y == m - 1:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 조건
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] == 1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    
print(dist[n - 1][m - 1])