n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 초기 윈도우(0번부터 k-1번까지)의 합을 구합니다.
curr_sum = sum(arr[:k])
max_sum = curr_sum

# 2. 윈도우를 오른쪽으로 한 칸씩 이동하며 O(1)로 갱신합니다.
for i in range(k, n):
    # 새로 들어온 원소 arr[i]를 더하고, 윈도우에서 벗어난 arr[i - k]를 뺍니다.
    curr_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, curr_sum)

print(max_sum)

# max_sum = 0

# for i in range(n - k + 1):
#     curr_sum = sum(arr[i: i + k])
#     max_sum = max(curr_sum, max_sum)

# print(max_sum)