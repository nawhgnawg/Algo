from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 모든 가능한 도시 좌표 (r, c) 리스트 생성
all_cities = [(r, c) for r in range(n) for c in range(n)]
# 기본 설정
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 

max_count = 0
for starts in combinations(all_cities, k):
    visited = [[False] * n for _ in range(n)]

    q = deque()

    # 선택된 k개의 시작 도시를 모두 큐에 넣고 방문 처리
    reachable_count = 0
    for r, c in starts:
        q.append((r, c))
        visited[r][c] = True
        reachable_count += 1

    count = 0
    # BFS 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 조건 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                h = abs(grid[x][y] - grid[nx][ny])
                # 높이 조건이 맞으면 탐색
                if u <= h <= d:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    reachable_count += 1
    max_count = max(max_count, reachable_count)

print(max_count)