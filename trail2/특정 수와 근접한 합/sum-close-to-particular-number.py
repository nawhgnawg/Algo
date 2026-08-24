from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 전체 합을 미리 구해둡니다. (O(N))
total_sum = sum(arr)
min_diff = float('inf')

# 2. 제외할 2개의 숫자를 고르는 2중 for문 (O(N^2))
for i in range(n):
    for j in range(i + 1, n):
        # 2개를 제외한 나머지 N-2개의 합을 O(1)로 계산
        curr_sum = total_sum - arr[i] - arr[j]
        diff = abs(curr_sum - s)
        
        min_diff = min(min_diff, diff)

print(min_diff)

# min_sum = float('inf')

# for comb in combinations(arr, n - 2):
#     curr_sum = abs(sum(comb) - s)
#     min_sum = min(curr_sum, min_sum)

# print(min_sum)



