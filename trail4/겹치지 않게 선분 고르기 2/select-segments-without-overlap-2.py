n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# 1. 선분들을 시작점 기준으로 오름차순 정렬
lines.sort()

# dp[i]: i번째 선분을 마지막으로 선택했을 때, 고를 수 있는 최대 선분의 수
dp = [1] * n

# 2. 앞에서부터 뒤로 순차적으로 진행
for i in range(n):
    # 3. 내(i) 앞에 있는 선분(j)들만 과거로 되돌아보며 탐색
    for j in range(n):
        # 4. 앞선 선분(j)의 끝점이 내 선분(i)의 시작점보다 작다면 (겹치지 않는다면)
        # (이미 정렬되어 있으므로, j 선분이 i 선분보다 뒤에 있을 걱정은 안 해도 된다!)
        if lines[j][1] < lines[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))