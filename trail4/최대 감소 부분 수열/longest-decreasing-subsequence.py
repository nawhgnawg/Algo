n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

# 1. 앞에서부터 뒤로 순차적으로 진행 (1부터 n-1까지)
for i in range(1, n):
    # 2. 내(i) 앞에 있는 원소(j)들 탐색
    for j in range(i):
        # 3. 내 앞에 있는 숫자가 '나보다 클 때만' 그 뒤에 줄을 설 수 있음 (감소해야 하므로)
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))