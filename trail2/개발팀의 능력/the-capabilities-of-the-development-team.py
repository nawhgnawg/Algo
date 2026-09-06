arr = list(map(int, input().split()))

total_sum = sum(arr)
min_dist = float('inf')

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(5):
            for l in range(k + 1, 5):
                if i == k or i == l or j == k or j == l:
                    continue
                
                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = total_sum - sum1 - sum2
                if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
                    continue

                dist = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
                min_dist = min(min_dist, dist)

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)
