n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 격자 내에 있는 모든 고유한 숫자들을 찾습니다.
# (이 숫자들을 한 번씩 '경로의 최솟값'으로 가정해 볼 것입니다)
unique_vals = set()
for i in range(n):
    for j in range(n):
        unique_vals.add(grid[i][j])

answer = float('inf')

# 2. L: "우리 경로에서 가장 작은 숫자는 무조건 L이야!" 라고 가정
for L in unique_vals:
    # 출발점 자체가 L보다 작다면, 출발조차 할 수 없으므로 이 가정은 무효!
    if grid[0][0] < L:
        continue

    # DP 테이블 초기화 (INF는 갈 수 없는 길을 의미함)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]

    # 1. 첫 번째 행 채우기 (왼쪽에서만 옴)
    for j in range(1, n):
        # 가정한 최솟값 L 이상일 때만 밟을 수 있음
        if grid[0][j] >= L:
            dp[0][j] = max(dp[0][j - 1], grid[0][j])

    # 2. 첫 번째 열 채우기 (위쪽에서만 옴)
    for i in range(1, n):
        if grid[i][0] >= L:
            dp[i][0] = max(dp[i - 1][0], grid[i][0])

    # 3. 나머지 칸 채우기
    for i in range(1, n):
        for j in range(1, n):
            # 밟으려는 칸이 L 이상일 때만 진행 가능
            if grid[i][j] >= L:
                # 위쪽과 왼쪽 경로 중 "기존 최댓값이 더 작은(유리한) 경로"를 선택 -> min()
                prev_best = min(dp[i - 1][j], dp[i][j - 1])

                if prev_best != float('inf'):
                    # 선택한 경로와 현재 칸의 숫자 중 더 큰 값이 이 경로의 새로운 최댓값이 됨 -> max()
                    dp[i][j] = max(prev_best, grid[i][j])
    
    # 4. 무사히 도착점에 도달했다면 차이 계산 및 갱신
    if dp[n - 1][n - 1] != float('inf'):
        current_diff = dp[n - 1][n - 1] - L
        answer = min(answer, current_diff)

print(answer)