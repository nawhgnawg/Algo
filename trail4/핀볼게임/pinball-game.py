n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상(0), 우(1), 하(2), 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 거울 반사 매핑 배열
mirror1 = [1, 0, 3, 2]  # '/' 거울 (1번)
mirror2 = [3, 2, 1, 0]  # '\' 거울 (2번)

def simulate(r, c, d):
    time = 1  # 처음 진입할 때 1초 소요
    
    while True:
        # 1. 현재 칸에 거울이 있다면 방향을 바꿈
        if grid[r][c] == 1:
            d = mirror1[d]
        elif grid[r][c] == 2:
            d = mirror2[d]
            
        # 2. 바라보는 방향으로 1칸 이동
        r += dx[d]
        c += dy[d]
        time += 1
        
        # 3. 격자 밖으로 빠져나갔다면 종료
        if r < 0 or r >= n or c < 0 or c >= n:
            return time

max_time = 0

# 4방향의 모든 테두리에서 출발해 보며 최댓값 찾기
for i in range(n):
    # 1. 윗면에서 아래(2)로 출발
    max_time = max(max_time, simulate(0, i, 2))
    # 2. 아랫면에서 위(0)로 출발
    max_time = max(max_time, simulate(n - 1, i, 0))
    # 3. 좌측면에서 우(1)로 출발
    max_time = max(max_time, simulate(i, 0, 1))
    # 4. 우측면에서 좌(3)로 출발
    max_time = max(max_time, simulate(i, n - 1, 3))

print(max_time)