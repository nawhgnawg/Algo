n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i] : 금액 i를 만들기 위해 필요한 '최대 동전의 수'
# 최댓값을 구해야 하므로, 불가능한 상태를 -1로 꽉 채워둡니다.
dp = [-1] * (m + 1)

# 0원을 만드는 데 필요한 동전은 0개입니다. (출발점)
dp[0] = 0

# 1원부터 목표 금액(m)까지 순서대로 최대 동전 개수를 채워나갑니다.
for i in range(1, m + 1):
    for coin in coins:
        # 조건 1. 목표 금액(i)이 동전의 가치보다 크거나 같고
        # 조건 2. 과거 금액(i - coin)을 만드는 방법이 존재할 때 (-1이 아닐 때)
        if i >= coin and dp[i - coin] != -1:
            # 기존 최대 개수와, 새로운 동전을 써서 만든 개수 중 더 큰 것을 선택!
            dp[i] = max(dp[i], dp[i - coin] + 1)

# 목표 금액(m)을 만들 수 없다면 -1 출력, 가능하다면 최대 동전 개수 출력
print(dp[m])