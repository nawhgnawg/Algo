import math

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

max_a = 0

for i in range(n):
    a[i] = a[i] / (2 ** (i + 1))
    max_a = max(max_a, a[i])

result = math.ceil(max_a)

print(result)
