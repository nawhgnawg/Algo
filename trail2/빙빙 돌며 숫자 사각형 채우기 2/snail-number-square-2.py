n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]

# 하, 우, 상, 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r, c = 0, 0
grid[r][c] = 1

dir = 0
count = 1

while count < (n * m):

    nr = r + dr[dir]
    nc = c + dc[dir]
    
    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
        count += 1
        grid[nr][nc] = count
        r, c = nr, nc 
    else:
        dir = (dir + 1) % 4

for row in grid:
    print(*row)
