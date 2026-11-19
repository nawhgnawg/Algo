n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find_rc(num):
    for r in range(n):
        for c in range(n):
            if grid[r][c] == num:
                return r, c

# 8방향 백터
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    for num in range(1, n * n + 1):
        r, c = find_rc(num)

        max_val = -1
        max_r, max_c = 0, 0

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] > max_val:
                    max_val = grid[nr][nc]
                    max_r, max_c = nr, nc

        # 특정 조건에 맞춰 교환
        grid[r][c], grid[max_r][max_c] = grid[max_r][max_c], grid[r][c]

for row in grid:
    print(*row)
