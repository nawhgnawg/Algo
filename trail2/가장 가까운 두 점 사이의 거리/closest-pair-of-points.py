from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist = float('inf')
for point in combinations(points, 2):
    (x1, y1), (x2, y2) = point
    dist = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    min_dist = min(min_dist, dist)

print(min_dist)


