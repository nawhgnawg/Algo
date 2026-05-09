from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_dist = float('inf')
for point in combinations(points, 2):
    (x1, y1), (x2, y2) = point
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    min_dist = min(min_dist, dist)

print(min_dist)


# min_dist = float('inf')
# for i in range(n):
#     for j in range(i + 1, n):
#         x1, y1 = points[i]
#         x2, y2 = points[j]
#         dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
#         min_dist = min(min_dist, dist)
