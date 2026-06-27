# 1. 넉넉하게 도화지와 오프셋을 준비합니다.
OFFSET = 100
MAX_R = 200

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    # 2. 오프셋을 더해 음수 좌표를 양수 인덱스로 변환합니다.
    x += OFFSET
    y += OFFSET
    
    # 3. 좌측 하단 꼭짓점부터 가로 8, 세로 8 크기만큼 색칠합니다.
    # 시작점(x)부터 시작점+8(x+8) 직전까지 1로 덮어씁니다.
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            grid[i][j] = 1

# 4. 색칠된 칸(1)의 총 개수를 셉니다.
total_area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            total_area += 1

print(total_area)