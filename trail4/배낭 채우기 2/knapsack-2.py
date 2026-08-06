n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i]: 보석을 담은 총 무게가 i일 때, 얻을 수 있는 최대 가치 
dp = [0] * (m + 1)


for i in range(n):
    w, v = arr[i]
    
    # 뒤에서부터 훑기
    # 보석을 딱 1번만 담을 수 있을 때: for j in range(m, w - 1, -1):
    # 보석을 여러 번 담을 수 있을 때: for j in range(w, m + 1):
    for j in range(w, m + 1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(max(dp))