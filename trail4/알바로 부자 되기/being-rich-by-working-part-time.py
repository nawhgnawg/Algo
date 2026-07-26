n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

info.sort()

# 1. dp[i]: i번째 알바를 선택했을 때, 얻을 수 있는 최대 금액
# dp = [0] * n
# dp[0] = info[0][2]

# 1. dp 초기화: 처음부터 각 알바를 단독으로 했을 때의 페이로 꽉 채워둡니다!
dp = [info[i][2] for i in range(n)]

# 2. 앞에서부터 뒤로 순차적으로 진행
for i in range(1, n):
    # 3. 내(i) 앞에 있는 스케줄(j)들만 탐색 
    for j in range(i):
        # 4. 앞선 스케줄의 끝나는 시간이 내 스케줄이 시작하는 시간보다 작다면
        if info[j][1] < info[i][0]:
            # 이미 기본 페이가 dp[i]에 들어있으므로, 과거의 기록(dp[j])을 더한 값과만 비교하면 됩니다!
            dp[i] = max(dp[i], dp[j] + info[i][2])

        
print(max(dp))
