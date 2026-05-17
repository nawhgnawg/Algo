n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


max_count = 0

for i in range(n):
    for j in range(n):
        
        temp_grid = []
        for x in range(n):
            row = []
            for y in range(n):
                row.append(grid[x][y])
            temp_grid.append(row)

        current_bomb = temp_grid[i][j]

        # 폭탄 터트리기
        for k in range(4):
            for l in range(current_bomb):
                nx = i + (dx[k] * l)
                ny = j + (dy[k] * l)

                if 0 <= nx < n and 0 <= ny < n:
                    if temp_grid[nx][ny] != 0:
                        temp_grid[nx][ny] = 0
        
        # 중력 적용
        for k in range(n):
            col = [temp_grid[l][k] for l in range(n)]

            current_col = [num for num in col if num != 0]
            new_col = [0] * (n - len(current_col)) + current_col

            for l in range(n):
                temp_grid[l][k] = new_col[l]

        count = 0
        # 최적의 십자 세기
        for x in range(n):
            for y in range(n):
                
                current_num = temp_grid[x][y]
                
                if current_num == 0:
                    continue

                # 하, 우 만 검사
                for d in range(1, 3):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if current_num == temp_grid[nx][ny]:
                            count += 1

        max_count = max(max_count, count)

print(max_count)
