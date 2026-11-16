from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

num_count = defaultdict(int)
min_len = float('inf')
left = 0

for right in range(n):
    num_count[arr[right]] += 1

    while num_count[1] >= k:
        current_len = right - left + 1
        if current_len < min_len:
            min_len = current_len

        num_count[arr[left]] -= 1
        left += 1


print(min_len if min_len != float('inf') else -1)