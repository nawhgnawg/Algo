n, m = map(int, input().split())
arr = list(map(int, input().split()))

# dp[i] : 합 i를 만들기 위해 고른 '최대 원소의 수' (또는 최소 원소의 수)
INF = float('inf')
# 최솟값을 찾아야 하므로, 초기값을 -1이 아니라 무한대(INF)로 꽉 채워줍니다.
dp = [INF] * (m + 1)
dp[0] = 0

# 1. 주어진 수열의 원소를 하나씩 살펴봅니다.
for num in arr:
    # 2. [가장 중요한 변화] 목표 합 m부터 num까지 "뒤에서부터(역순으로)" 훑습니다!
    # 이렇게 해야 원소를 중복해서 사용하는 것을 막을 수 있습니다.
    for i in range(m, num - 1, -1):
        # 3. 과거의 합(i - num)을 만드는 방법이 존재한다면 갱신!
        if dp[i - num] != -1:
            dp[i] = min(dp[i], dp[i - num] + 1)

# 목표 합(m)을 도저히 만들 수 없다면 -1 출력
if dp[m] == INF:
    print(-1)
else:
    print(dp[m])