from itertools import combinations

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_dist = float('inf')

for comb in combinations(points, m):

    max_dist = 0

    # 선택된 점들 중 가장 먼 점 찾기
    for point1, point2 in combinations(comb, 2):
        x1, y1 = point1
        x2, y2 = point2

        # 거리 계산
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

        # 최대값 찾기
        max_dist = max(dist, max_dist)

    # 최솟값 갱신
    min_dist = min(max_dist, min_dist)

print(min_dist)
    