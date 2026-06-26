n = int(input())

# 1. 2차원 격자(도화지) 생성
# 좌표 범위가 보통 -100 ~ 100이라고 가정할 때, 
# 음수 인덱스 방지를 위해 모든 좌표에 100을 더해 0 ~ 200으로 만듭니다.
OFFSET = 100
MAX_R = 200

# 201 x 201 크기의 0으로 채워진 격자 생성
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 2. 오프셋을 더해 양수 인덱스로 변환
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    # 3. 직사각형 넓이만큼 격자에 색칠 (1로 덮어쓰기)
    # 격자 '칸'을 칠하는 것이므로 x2, y2 전까지 반복합니다.
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

# 4. 색칠된 칸(1)의 총 개수 세기
total_area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            total_area += 1

print(total_area)