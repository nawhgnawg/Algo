n = int(input())
arr = list(map(int, input().split()))

# 1. 전체 합과, 우리가 목표로 하는 '절반'의 값을 구합니다.
total_sum = sum(arr)
target = total_sum // 2

# dp[i] : 주어진 숫자를 1번씩만 조합해서 합 i를 만들 수 있는지 여부 (True / False)
dp = [False] * (total_sum + 1)

# 합 0은 아무것도 고르지 않으면 되므로 항상 가능합니다.
dp[0] = True

# 2. 각 숫자를 딱 한 번씩만 쓰기 위해, '뒤에서부터(역순)' 훑습니다!
for num in arr:
    for i in range(total_sum, num - 1, -1):
        # 과거에 (i - num) 합을 만드는 것이 가능했다면, 
        # 거기에 num을 더한 합(i)도 당연히 가능해집니다!
        if dp[i - num]:
            dp[i] = True

# 3. 목표치(절반)부터 0까지 거꾸로 내려오면서, 가장 먼저 만들 수 있는 합(True)을 찾습니다.
# target에서 시작해서 내려가므로, 이것이 '절반에 가장 가까운 합'이 됩니다.
answer = 0
for i in range(target, -1, -1):
    if dp[i]:
        # 한 그룹의 합이 i로 결정되었습니다.
        # 두 그룹의 차이는 (전체 합 - i) - i 이므로 아래와 같습니다.
        answer = total_sum - (2 * i)
        break

print(answer)