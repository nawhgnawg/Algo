n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
current_sum = 0
left = 0

for right in range(n):
    current_sum += arr[right]

    while current_sum > m:
        current_sum -= arr[left]
        left += 1
    
    if current_sum == m:
        answer += 1

print(answer)