n = int(input())
arr = list(map(int, input().split()))

# dp[i] : i번째 칸에 도달하기까지의 최대 점프 횟수
# 아직 도달하지 못한 칸은 -1로 초기화 
dp = [-1] * n
dp[0] = 0  # 시작점은 점프 횟수 0

for i in range(n):
    # 1. 만약 현재 위치(i)에 도달한 적이 없다면(-1), 여기서 출발할 수도 없으므로 건너뜀
    if dp[i] == -1:
        continue
    
    # 2. 현재 위치 i에서 갈 수 있는 j 탐색
    for j in range(i + 1, min(i + arr[i] + 1, n)):
        # 3. j번째 칸에 도달하는 최대 점프 횟수 갱신
        # 기존에 j칸에 도달했던 횟수(dp[j])와 
        # 지금 i칸을 거쳐서 1번 더 점프해 j칸으로 가는 횟수(dp[i] + 1) 중 더 큰 값!
        dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
