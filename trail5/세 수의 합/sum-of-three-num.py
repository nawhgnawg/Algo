from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

# 1. 첫 번째 수 arr[i]를 고정
for i in range(n - 2):
    target = k - arr[i]
    freq = defaultdict(int)
    
    # 2. i 이후의 구간(i+1 ~ n-1)에서 '두 수의 합이 target'이 되는 쌍 찾기
    for j in range(i + 1, n):
        needed = target - arr[j]
        
        # 필요한 수가 이전에 등장했다면 정답에 개수 추가
        if needed in freq:
            ans += freq[needed]
            
        # 현재 수 arr[j]의 등장 횟수 누적
        freq[arr[j]] += 1

print(ans)