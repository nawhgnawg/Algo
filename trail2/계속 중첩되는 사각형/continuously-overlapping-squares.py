OFFSET = 100
MAX_R = 200

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

n = int(input())

is_blue = False

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    if i % 2 == 0:
        color = 1  # 빨간색
    else:
        color = 2  # 파란색

    # 격자 칸 정석대로 색칠하기
    for r in range(x1, x2):
        for c in range(y1, y2):
            grid[r][c] = color

total_area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 2:
            total_area += 1

print(total_area)