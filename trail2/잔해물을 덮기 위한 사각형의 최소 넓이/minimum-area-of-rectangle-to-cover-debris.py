OFFSET = 1000
MAX_R = 2000

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

# 1. 첫 번째 사각형(잔해) 색칠하기
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

# [주의] 칸을 칠하는 것이므로 끝점 x2, y2는 포함하지 않습니다!
for i in range(x1, x2):
    for j in range(y1, y2):
        grid[i][j] = 1

# 2. 두 번째 사각형으로 덮어 지우기
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

for i in range(x1, x2):
    for j in range(y1, y2):
        grid[i][j] = 0

# 3. 남아있는 잔해(1)들의 최소/최대 좌표 찾기
min_x, max_x = MAX_R + 1, -1
min_y, max_y = MAX_R + 1, -1
is_remaining = False # 잔해가 하나라도 남아있는지 확인하는 플래그

for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            is_remaining = True
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j

# 4. 최소 직사각형 넓이 계산 및 출력
if not is_remaining:
    # 두 번째 사각형이 첫 번째 사각형을 완벽히 다 덮어서 잔해가 0인 경우
    print(0)
else:
    # (최댓값 - 최솟값 + 1) 로 가로, 세로 길이를 구해 곱합니다.
    # (+1을 하는 이유는, 인덱스 1부터 1까지 칠해져 있다면 길이 1칸이기 때문입니다: 1 - 1 + 1 = 1)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)

