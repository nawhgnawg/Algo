n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n - k + 1):
    curr_sum = sum(arr[i: i + k])
    max_sum = max(curr_sum, max_sum)

print(max_sum)