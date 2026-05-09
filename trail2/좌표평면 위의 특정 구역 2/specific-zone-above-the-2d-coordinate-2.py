n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


# 남은 점들로 만들 수 있는 사각형 = (최대 x - 최소 x) * (최대 y - 최소 y)
rectangles = []

for x, y in points:
    dis_x = x
    dis_y = y

    curr_x = []
    curr_y = []
    for r, c in points:
        if r == x and c == y:
            continue
        curr_x.append(r)
        curr_y.append(c)
    
    width = (max(curr_x) - min(curr_x)) * (max(curr_y) - min(curr_y))
    rectangles.append(width)

print(min(rectangles))

    
    


