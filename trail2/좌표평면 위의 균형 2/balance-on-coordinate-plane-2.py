n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

answer = []
min_val = float('inf')

for i in range(0, max(x_points) + 1, 2):
    for j in range(0, max(y_points) + 1, 2):
        x_line = i
        y_line = j

        # 좌하단, 우하단, 좌상단, 우상단
        div = [0, 0, 0, 0]
        
        for x, y in points:
            if 0 <= x < x_line and 0 <= y < y_line:
                div[0] += 1
            if x > x_line and 0 <= y < y_line:
                div[1] += 1
            if 0 <= x < x_line and y > y_line:
                div[2] += 1
            if x > x_line and y > y_line:
                div[3] += 1

        val = 0
        for k in range(4):
            val += max(div) - div[k]
            min_val = min(min_val, val)
            answer.append((min_val, max(div)))

answer.sort()
print(answer[0][1])


    