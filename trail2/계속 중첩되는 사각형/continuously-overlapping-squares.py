OFFSET = 100
MAX_R = 200

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

n = int(input())

is_blue = False

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            if is_blue:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    if not is_blue:
        is_blue = True
    else:
        is_blue = False

total_area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            total_area += 1

print(total_area)