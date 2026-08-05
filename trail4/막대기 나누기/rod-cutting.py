n = int(input())

# 막대기 길이 1부터 n까지의 가격 배열
# 예) prices[1] = 길이 1의 가격, prices[2] = 길이 2의 가격
prices = [0] + list(map(int, input().split()))

# dp[i] : 길이가 i인 막대기를 팔아서 얻을 수 있는 '최대 수익'
dp = [0] * (n + 1)

# 1. 자를 수 있는 조각의 길이(i)를 1부터 n까지 하나씩 살펴봅니다. (마치 동전 종류를 보듯)
for i in range(1, n + 1):
    # 2. [황금 규칙] 중복해서 자를 수 있으므로, i부터 n까지 '앞에서부터' 훑습니다!
    for j in range(i, n + 1):
        # 3. 기존에 길이 j를 팔아서 얻은 최대 수익과,
        # (j - i) 길이를 팔았을 때의 수익 + 이번 조각(i)을 팔았을 때의 수익(prices[i]) 중 더 큰 값 선택!
        # print(f'{i, j} => dp[j] = max({dp[j]}, {dp[j - i] + prices[i]})', end=' ')
        dp[j] = max(dp[j], dp[j - i] + prices[i])
        # print(dp)
print(dp[n])

