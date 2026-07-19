n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]

# 1. 첫 번째 행 채우기 (왼쪽에서 오른쪽으로 오는 경우)
for j in range(1, n):
    dp[0][j] = min(dp[0][j - 1], grid[0][j])

# 2. 첫 번째 열 채우기 (위에서 아래로 오는 경우)
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0], grid[i][0])


# 3. 나머지 칸 채우기
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[n - 1][n - 1])