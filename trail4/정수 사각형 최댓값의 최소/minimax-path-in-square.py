n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]

# 1. 첫 번째 행 채우기 (왼쪽에서만 옴)
for j in range(n):
    dp[0][j] = max(dp[0][j-1], grid[0][j])

# 2. 첫 번째 열 채우기 (위쪽에서만 옴)
for i in range(n):
    dp[i][0] = max(dp[i-1][0], grid[i][0])

# 1 4 4
# 3 4 4
# 5 4 2

# 3. 나머지 칸 채우기
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])