n = int(input())
arr = list(map(int, input().split()))

answer = float('inf')

for i in range(n):
    dist_sum = 0
    for j in range(n):
        if i == j:
            continue
        dist_sum += (arr[j] * abs(i - j))
    
    answer = min(answer, dist_sum)

print(answer)
