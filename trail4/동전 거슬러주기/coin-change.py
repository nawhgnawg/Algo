n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i] = dp[i - 3] + 1
# dp[i] : 금액 i를 만들기 위해 필요한 '최소 동전의 수'
# 처음에는 절대 도달할 수 없는 무한대(INF) 값으로 꽉 채워둡니다.
INF = float('inf')
dp = [INF] * (m + 1)

# 0원을 만드는 데 필요한 동전은 0개입니다. (출발점)
dp[0] = 0

for i in range(1, m + 1):
    for coin in coins:
        # 조건 1. 목표 금액(i)이 동전의 가치보다 크거나 같아야 그 동전을 낼 수 있습니다.
        # 조건 2. 동전을 내기 전의 과거 금액(i - coin)을 만드는 방법이 존재해야 합니다.
        if i >= coin and dp[i - coin] != INF:
            # 기존에 알고 있던 방법과, 새로운 동전을 써서 만든 방법 중 더 적은 개수를 선택!
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 목표 금액(m)을 도저히 만들 수 없다면 -1 출력, 가능하다면 최소 동전 개수 출력
if dp[m] == INF:
    print(-1)
else:
    print(dp[m])