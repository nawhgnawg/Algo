n, m = map(int, input().split())
grid = [[''] * m for _ in range(n)]

# A = chr(65) ~ Z = chr(90), 26개
alpa = []
for i in range(26):
    alpa.append(chr(65 + i))

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = 0, 0
grid[r][c] = alpa[0]

dir = 0
count = 1
i = 0

while count < (n * m):
    nr = r + dr[dir]
    nc = c + dc[dir]

    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '':
        count += 1
        i += 1
        if i >= 26:
            i -= 26
            
        grid[nr][nc] = alpa[i]
        r = nr
        c = nc
    else:
        dir = (dir + 1) % 4
    
for row in grid:
    print(*row)

