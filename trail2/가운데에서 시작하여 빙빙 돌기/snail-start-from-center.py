n = int(input())
grid = [[0] * n for _ in range(n)]

# 좌, 상, 우, 하
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 시작점
r, c = n - 1, n - 1
grid[r][c] = n * n

dir = 0
count = n * n


for _ in range(n * n - 1):
    nr = r + dr[dir]
    nc = c + dc[dir]

    if not (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0):
        dir = (dir + 1) % 4
        nr = r + dr[dir]
        nc = c + dc[dir]
    
    count -= 1
    grid[nr][nc] = count
    r = nr
    c = nc

for row in grid:
    print(*row)
    
