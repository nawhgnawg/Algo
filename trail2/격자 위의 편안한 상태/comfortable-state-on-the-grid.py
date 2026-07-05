n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * n for _ in range(n)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


for r, c in points:
    r -= 1
    c -= 1
    grid[r][c] = 1  # 색칠

    count = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)



