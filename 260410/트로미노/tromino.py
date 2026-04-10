n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

# 1. 가로 일자 블록(1 x 3) 탐색
for i in range(n):
    for j in range(m - 2):
        current_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_sum = max(current_sum, max_sum)

# 2. 세로 일자 블록(3 x 1) 탐색
for i in range(n - 2):
    for j in range(m):
        current_sum = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
        max_sum = max(current_sum, max_sum)

# 3. 'ㄴ' 자 블록 탐색
for i in range(n - 1):
    for j in range(m - 1):
        # 2 x 2 블록을 구함
        square_sum = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]

        # 하나씩 뺀 값을 구함
        shape1 = square_sum - grid[i][j]
        shape2 = square_sum - grid[i][j + 1]
        shape3 = square_sum - grid[i + 1][j]
        shape4 = square_sum - grid[i + 1][j + 1]

        max_sum = max(shape1, shape2, shape3, shape4, max_sum)

print(max_sum)
        