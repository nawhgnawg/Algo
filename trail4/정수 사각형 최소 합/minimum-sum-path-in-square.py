n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][n - 1] = grid[0][n - 1]


# 1. 첫 번째 행 채우기 (오른쪽에서 오는 경로밖에 없음)
for j in range(n - 2, -1, -1):
    dp[0][j] = dp[0][j + 1] + grid[0][j]

# 2. n 번째 열 채우기 (위에서 오는 경로밖에 없음)
for i in range(1, n):
    dp[i][n - 1] = dp[i - 1][n - 1] + grid[i][n - 1]

# 3. 나머지 칸 채우기 (위쪽과 왼쪽 중 더 큰 값 선택해서 현재 값을 더함)
for i in range(1, n):               # 1번 행부터 n - 1번 행까지 순차적으로 내려옴
    for j in range(n - 2, -1, -1):  # 오른쪽에서 왼쪽으로 이동
        dp[i][j] = min(dp[i][j + 1], dp[i - 1][j]) + grid[i][j]

print(dp[n - 1][0])

    
