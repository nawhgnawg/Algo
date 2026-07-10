n, t = map(int, input().split())
commands = input().strip()
grid = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c = n // 2, n // 2
d_idx = 0
total = grid[r][c]

for cmd in commands:
    if cmd == 'R':
        d_idx = (d_idx + 1) % 4
    elif cmd == 'L':
        d_idx = (d_idx + 3) % 4
    elif cmd == 'F':
        nr = r + dr[d_idx]
        nc = c + dc[d_idx]

        if 0 <= nr < n and 0 <= nc < n:
            total += grid[nr][nc]
            r = nr
            c = nc

print(total)