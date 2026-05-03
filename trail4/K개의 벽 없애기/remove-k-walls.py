from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# (0, 0) -> (3, 3) : 2개의 벽을 없애서 걸리는 최소시간

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = {}
q = deque()
q.append((r1, c1, 0))
dist[(r1, c1, 0)] = 0

ans = -1

while q:
    x, y, w = q.popleft()

    # 목적지에 도달하면 최단 시간 갱신
    if x == r2 and y == c2:
        if ans == -1 or dist[(x, y, w)] < ans:
            ans = dist[(x, y, w)]
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 갈 수 있음
            if grid[nx][ny] == 0:
                if (nx, ny, w) not in dist:
                    q.append((nx, ny, w))
                    dist[(nx, ny, w)] = dist[(x, y, w)] + 1
            elif grid[nx][ny] == 1:
                if w < k and (nx, ny, w + 1) not in dist:
                    q.append((nx, ny, w + 1))
                    dist[(nx, ny, w + 1)] = dist[(x, y, w)] + 1
                
print(ans)