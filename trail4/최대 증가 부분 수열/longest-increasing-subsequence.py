n = int(input())
arr = list(map(int, input().split()))

# dp[i] : i번째 원소를 마지막으로 하는 LIS의 길이
# 처음에는 모두 자기 자신만 포함하므로 1로 초기화
dp = [1] * n

# 1. 두 번째 숫자부터 끝까지 순서대로 하나씩 도착점(i)으로 삼아 계산
for i in range(n):
    # 2. 내(i) 앞에 있는 모든 숫자(j)들을 과거로 되돌아보며 탐색
    for j in range(i):
        # 3. 나보다 작은 숫자를 발견했다면, 그 숫자 뒤에 이어 붙임
        if arr[j] < arr[i]:
            # j번째 숫자의 수열에 나를 붙인 길이(dp[j] + 1)와 
            # 기존에 내가 알고 있던 최대 길이(dp[i]) 중 더 큰 값으로 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
