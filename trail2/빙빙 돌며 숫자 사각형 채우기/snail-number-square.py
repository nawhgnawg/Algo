n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_count = n * m
x, y = 0, 0 # 현재 위치
d = 0       # 현재 방향
# i = 1       # 현재 카운트
grid[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dx[d], y + dy[d]
    
    # 3. 만약 다음 칸이 맵을 벗어나거나 이미 방문한 곳이라면?
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        d = (d + 1) % 4       # 방향을 90도 틀고
        nx, ny = x + dx[d], y + dy[d] # 바꾼 방향으로 다음 칸 다시 계산!
    
    # 4. 검증이 끝난 안전한 칸으로 이동 후 숫자 쾅!
    x, y = nx, ny
    grid[x][y] = i

# while i < max_count:

#     nx = x + dx[d]
#     ny = y + dy[d]
#     # 범위 안이 아니거나 이미 거쳐간 곳이라면
#     if not in_range(nx, ny) or grid[nx][ny] != 0:
#         d = (d + 1) % 4
#     else:
#         i += 1
#         grid[nx][ny] = i
#         x = nx
#         y = ny

for row in grid:
    print(*row)

