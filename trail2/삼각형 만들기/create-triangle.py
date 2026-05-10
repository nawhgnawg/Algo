from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_area = 0

for (x1,y1), (x2,y2), (x3,y3) in combinations(points, 3):
    # x축 평행한 변 존재 여부 (y좌표 같은 쌍)
    x_parallel = (y1 == y2) or (y2 == y3) or (y1 == y3)
    # y축 평행한 변 존재 여부 (x좌표 같은 쌍)
    y_parallel = (x1 == x2) or (x2 == x3) or (x1 == x3)

    if x_parallel and y_parallel:
        # 넓이 = 밑변 * 높이 / 2
        # 힌트의 공식 사용 (넓이 * 2 = 절댓값)
        area2 = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
        max_area = max(max_area, area2)

print(max_area)