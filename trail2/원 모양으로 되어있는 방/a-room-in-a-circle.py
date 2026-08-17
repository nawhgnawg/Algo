n = int(input())
info = [int(input()) for i in range(n)]

min_dist = float('inf')

# 시작점
for i in range(n):
    curr_dist = 0
    curr_info = info[i:] + info[:i]
    for j in range(1, n):
        curr_dist += curr_info[j] * j
    min_dist = min(curr_dist, min_dist)

print(min_dist)