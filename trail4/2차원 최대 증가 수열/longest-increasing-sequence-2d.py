n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: (i, j)칸을 마지막으로 밟았을 때 방문한 최대 칸의 수
# -1은 아직 도달하지 못한 칸을 의미함
dp = [[-1] * m for _ in range(n)]

# 시작점 세팅 (첫 칸을 밟았으므로 길이는 1)
dp[0][0] = 1

# 1. 2중 for문으로 '현재 발판이 될 위치(i, j)'를 순서대로 탐색합니다.
for i in range(n):
    for j in range(m):
        # 현재 위치에 도달한 적이 없다면 여기서 출발할 수 없으므로 패스
        if dp[i][j] == -1:
            continue
        
        # 2. 현재 위치(i, j)에서 점프할 '미래의 목적지(ni, nj)'를 탐색합니다.
        # 조건: 행과 열이 모두 현재 위치보다 커야 함 (오른쪽 아래 방향)
        for ni in range(i + 1, n):
            for nj in range(j + 1, m):
                # 조건: 뛰려는 목적지의 숫자가 현재 밟고 있는 숫자보다 커야 함
                if grid[ni][nj] > grid[i][j]:
                    # 미래 칸에 기록된 기존 길이와, 현재 칸에서 1칸 더 뛰어 넘어간 길이 중 최댓값 갱신!
                    dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)

# 3. DP 테이블 전체를 뒤져서 가장 컸던 값(가장 긴 수열의 길이)을 찾습니다.
answer = -1
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])

print(answer)
