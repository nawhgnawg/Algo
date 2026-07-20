n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 모든 칸의 정보를 (값, x, y) 형태로 리스트에 담고 오름차순 정렬
cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

# 값이 작은 순서대로 정렬
cells.sort()

# DP 테이블: 각 칸을 마지막으로 밟았을 때의 최대 경로 길이
# 처음에는 어떤 칸에서 시작하든 자기 자신만 밟으므로 길이는 무조건 1
dp = [[1] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1

# 2. 값이 가장 작은 칸부터 순서대로 꺼내며 DP 값 갱신
for value, x, y in cells:
    # 현재 칸(x, y)의 상하좌우를 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 격자 범위 안이고, 나(value)보다 작은 숫자에서 건너올 수 있다면?
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] < value:
            # 이전 칸(nx, ny)까지의 최대 길이에 +1을 한 값과 현재 값을 비교해 갱신
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    
    # DP가 갱신될 때마다 전체 최댓값도 같이 갱신해 줍니다.
    answer = max(answer, dp[x][y])

print(answer)