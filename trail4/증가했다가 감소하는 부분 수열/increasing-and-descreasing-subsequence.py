n = int(input())
arr = list(map(int, input().split()))

# 각각 자기 자신만 포함하는 길이 1로 초기화
up_dp = [1] * n
down_dp = [1] * n

# 1. 앞에서부터 순차적으로 탐색
for i in range(1, n):
    for j in range(i):
        # 2. [증가 상태] 내(i)가 앞의 숫자(j)보다 크다면 -> 계속 올라갈 수 있음!
        if arr[j] < arr[i]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)
        # 3. [감소 상태] 내(i)가 앞의 숫자(j)보다 작다면 -> 내려가야 함!
        elif arr[j] > arr[i]:
            # 여기서 가장 중요한 핵심 로직!
            # 1) 이미 내려가고 있던 수열(down_dp) 뒤에 계속 이어서 내려가거나
            # 2) 방금 전까지 올라가고 있던 수열(up_dp)에서 '지금부터' 꺾어서 내려가거나!
            down_dp[i] = max(down_dp[i], down_dp[j] + 1, up_dp[j] + 1)

# 4. 모든 배열을 뒤져서 '계속 올라간 것'과 '올라가다 내려온 것' 중 가장 긴 길이를 찾음
answer = 0
for i in range(n):
    answer = max(answer, up_dp[i], down_dp[i])

print(answer)