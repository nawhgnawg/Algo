from collections import deque

n, r, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]


# 상하좌우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]

result = []

q = deque([(r - 1, c - 1)])
visited[r - 1][c - 1] = True
result.append(a[r - 1][c - 1])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and a[nx][ny] > a[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
                result.append(a[nx][ny])
                break

for num in result:
    print(num, end=' ')

