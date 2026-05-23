n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

count = [0] * 102

for a, b in segments:
    for i in range(a, b + 1):
        count[i] += 1

print(max(count))