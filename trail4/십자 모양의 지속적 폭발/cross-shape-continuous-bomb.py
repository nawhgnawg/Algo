n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]



for command in commands:

    # 인덱스 정렬
    command -= 1
    all_zero = True

    for i in range(n):
        if grid[i][command] != 0:
            current_bomb = grid[i][command]
            x, y = i, command
            grid[x][y] = 0
            all_zero = False
            break

    if all_zero:
        break

    # 폭탄 터지기
    for i in range(4):
        for j in range(current_bomb):
            nx = x + (dx[i] * j)
            ny = y + (dy[i] * j)
        
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] != 0:
                    grid[nx][ny] = 0
    
    # 중력 작용
    for j in range(n):
        col = [grid[i][j] for i in range(n)]
        
        count = 0
        
        curr_col = []
        for num in col:
            if num != 0:
                count += 1
                curr_col.append(num)
        new_col = [0] * (n - count) + curr_col

        # grid 업데이트
        for i in range(n):
            grid[i][j] = new_col[i]


for row in grid:
    print(*(row))


# 1 0 2 3
# 3 2 2 3
# 3 1 6 2
# 4 5 4 4

# 0 0 0 3
# 1 0 2 3
# 3 0 6 2
# 4 5 4 4

# 0 0 0 3
# 1 0 2 3
# 3 0 6 2
# 4 0 4 4

# 0 0 0 3
# 1 0 2 3
# 3 0 6 2
# 4 0 4 4