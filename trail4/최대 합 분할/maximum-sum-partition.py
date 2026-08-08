n = int(input())
arr = list(map(int, input().split()))

# 조건: A랑 B의 합이 같고, 최대가 되어야함
total = sum(arr)

offset = total  # 차이(diff)는 -total ~ total 범위이므로, 배열 인덱스는 diff + offset
size = 2 * total + 1

# dp[i]: 지금까지 처리한 숫자들로 (sumA - sumB) = (i - offset) 을 만들 때, 가능한 sumA의 최댓값
dp = [-1] * size
dp[offset] = 0      # 아무것도 안골랐을 때: 차이 0, sumA = 0

for x in arr:
    new_dp = dp[:]  # x를 C에 넣는 경우 = 상태 변화 없음 
    for i in range(size):
        if dp[i] == -1:
            continue

        # x를 A에 넣는 경우: 차이가 x만큼 증가, sumA도 x만큼 증가
        ni = i + x
        if ni < size and dp[i] + x > new_dp[ni]:
            new_dp[ni] = dp[i] + x
         # x를 B에 넣는 경우: 차이가 x만큼 감소, sumA는 그대로
        ni2 = i - x
        if ni2 >= 0 and dp[i] > new_dp[ni2]:
            new_dp[ni2] = dp[i]
    
    dp = new_dp

print(dp[offset])   # 차이가 0 일때 최대 sumA


