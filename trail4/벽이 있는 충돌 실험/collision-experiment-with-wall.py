t = int(input())

# 상, 하, 좌, 우
DIR = {
    'U': (-1, 0, 'D'),
    'D': (1, 0, 'U'),
    'L': (0, -1, 'R'),
    'R': (0, 1, 'L'),
}

for _ in range(t):
    n, m = map(int, input().split())
    grid = [[''] * n for _ in range(n)]

    # 구슬의 위치와 방향
    for _ in range(m):
            r, c, d = input().split()
            grid[int(r) - 1][int(c) - 1] = d

    # 2 * n초 이후에는 추가 충돌이 발생하지 않음
    for _ in range(2 * n):
        next_grid = [[''] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if not grid[r][c]:
                    continue
                
                dr, dc, opp_d = DIR[grid[r][c]]
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    next_grid[nr][nc] = grid[r][c]
                    count[nr][nc] += 1
                else:
                    next_grid[r][c] = opp_d
                    count[r][c] += 1

        for r in range(n):
            for c in range(n):
                if count[r][c] > 1:
                    next_grid[r][c] = ''
        
        grid = next_grid
    
    ans = sum(1 for r in range(n) for c in range(n) if grid[r][c])
    print(ans)


