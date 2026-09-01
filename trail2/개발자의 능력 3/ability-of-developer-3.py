abilities = list(map(int, input().split()))

n = len(abilities)

total = sum(abilities)

min_dist = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_a = abilities[i] + abilities[j] + abilities[k]
            sum_b = total - sum_a
            dist = abs(sum_a - sum_b)
            min_dist = min(dist, min_dist)

print(min_dist)