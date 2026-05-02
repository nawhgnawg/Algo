from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = [[0] * n for _ in range(n)]

q = deque()
dist = [[-1] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if grid[r][c] == 3:
            q.append((r, c))
            dist[r][c] = 0


while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and grid[nx][ny] != 1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
                    

# 4. 출력 형식에 맞춰 결과 출력
for r in range(n):
    row_result = []
    for c in range(n):
        if grid[r][c] == 2:
            # 해당 칸에 사람이 있었다면 최단 거리(또는 도달 불가 시 -1) 출력
            row_result.append(dist[r][c])
        else:
            # 사람이 없던 칸은 0 출력
            row_result.append(0)
    print(*(row_result))