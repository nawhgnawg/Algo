n = int(input())
a = list(map(int, input().split()))

max_pairs = 0

for k in range(1, max(a) + 1):
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] - k == k - a[i]:
                pairs += 1

    max_pairs = max(max_pairs, pairs)

print(max_pairs)

        
