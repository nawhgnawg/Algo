from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 탐색할 K의 최대값
max_k = 0
for row in grid:
    max_k = max(max(row), max_k)

best_k = 1
max_safe_zones = 0

for k in range(1, max_k + 1):

    visited = [[False] * m for _ in range(n)]
    current_safe_zones = 0

    # 출발점 찾기
    for i in range(n):
        for j in range(m):
            # 아직 물에 잠기지 않았고, 아직 방문하지 않은 새로운 안전 영역
            if grid[i][j] > k and not visited[i][j]:
                current_safe_zones += 1

                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]

                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            if grid[nx][ny] > k:
                                visited[nx][ny] = True
                                q.append((nx, ny))


    # 최대값 갱신하기
    if current_safe_zones > max_safe_zones:
        max_safe_zones = current_safe_zones
        best_k = k

print(best_k, max_safe_zones)