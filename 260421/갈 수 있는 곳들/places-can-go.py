from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기록
visited = [[False] * n for _ in range(n)]

# 방문이 가능한 서로 다른 칸의 수
total = 0
# 1
q = deque()
for r, c in points:
    q.append((r - 1, c - 1))
    if not visited[r - 1][c - 1]:
        visited[r - 1][c - 1] = True
        total += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    total += 1

print(total)