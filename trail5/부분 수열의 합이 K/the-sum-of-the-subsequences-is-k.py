import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합의 등장 횟수를 저장할 해시맵
# pref_count[x]: 누적 합 값이 x인 위치의 개수
pref_count = defaultdict(int)

# 초기 상태: 아무것도 선택하지 않았을 때 누적 합 0은 1개 존재
pref_count[0] = 1

current_sum = 0
ans = 0

for num in arr:
    current_sum += num
    
    # current_sum - k가 이전에 등장한 적이 있다면,
    # 그 지점부터 현재까지의 구간 합이 정확히 k가 됨
    target = current_sum - k
    if target in pref_count:
        ans += pref_count[target]
        
    # 현재 누적 합의 카운트 증가
    pref_count[current_sum] += 1

print(ans)