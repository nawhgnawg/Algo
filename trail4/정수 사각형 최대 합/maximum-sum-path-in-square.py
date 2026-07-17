# from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 이전까지의 최대 합을 저장할 DP 테이블 
dp = [[0] * n for _ in range(n)]

# 1. 시작점 세팅
dp[0][0] = grid[0][0]

# 2. 첫 번째 행 채우기 (왼쪽에서 오는 경로밖에 없음)
for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + grid[0][j]

# 3. 첫 번째 열 채우기 (위에서 오는 경로밖에 없음)
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + grid[i][0]

# 4. 나머지 칸 채우기 (위쪽과 왼쪽 중에서 더 큰 값을 채움)
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

print(dp[n - 1][n - 1])


# BFS는 시간 초과 또는 메모리 초과 발생
# # 우, 하
# dx, dy = [0, 1], [1, 0]

# dist = [[0] * n for _ in range(n)]

# # 시작
# q = deque([(0, 0, grid[0][0])])

# # 이전최대를 계속 축적
# while q:
#     x, y, prev_sum = q.popleft()

#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             q.append((nx, ny, prev_sum + grid[nx][ny]))
#             dist[nx][ny] = max(dist[nx][ny], prev_sum + grid[nx][ny])

# print(dist[n - 1][n - 1])
