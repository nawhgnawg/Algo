from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start_points = []
for _ in range(k):
    r, c = map(int, input().split())
    start_points.append((r - 1, c - 1))

# 돌들의 위치 미리 파악
stones = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_visited = 0

for removed_stones in combinations(stones, m):
    # 임시로 돌을 치움 (0으로 변경)
    for r, c in removed_stones:
        grid[r][c] = 0

    # BFS를 통한 방문 가능 칸 계산
    q = deque(start_points)
    visited = [[False] * n for _ in range(n)]
    count = 0

    for r, c in start_points:
        visited[r][c] = True
        count += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    
    # 최대값 갱신
    max_visited = max(max_visited, count)
    
    # 다음 조합을 위해 원상복구
    for r, c in removed_stones:
        grid[r][c] = 1

print(max_visited)