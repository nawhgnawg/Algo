n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_area = float('inf')

for i in range(n):
    # 인덱스 하나만 제거
    remaining = [points[j] for j in range(n) if j != i]

    xs = [x for x, y in remaining]
    ys = [y for x, y in remaining]

    area = (max(xs) - min(xs)) * (max(ys) - min(ys))
    min_area = min(min_area, area)

print(min_area)

# rectangles = []
# for x, y in points:
#     dis_x = x
#     dis_y = y

#     curr_x = []
#     curr_y = []
#     for r, c in points:
#         if r == x and c == y:
#             continue
#         curr_x.append(r)
#         curr_y.append(c)
    
#     width = (max(curr_x) - min(curr_x)) * (max(curr_y) - min(curr_y))
#     rectangles.append(width)

# print(min(rectangles))