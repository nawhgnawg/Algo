n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 방향: 0(남), 1(서), 2(북), 3(동)
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

def get_start_pos_and_dir(k, n):
    if k <= n:
        return 0, k - 1, 0           # 위 -> 아래 (남)
    elif k <= 2 * n:
        return k - n - 1, n - 1, 1   # 우 -> 좌 (서)
    elif k <= 3 * n:
        return n - 1, 3 * n - k, 2   # 아래 -> 위 (북)
    else:
        return 4 * n - k, 0, 3       # 좌 -> 우 (동)

# 1. 시작 좌표와 방향 얻기
r, c, curr_dir = get_start_pos_and_dir(k, n)

count = 0

# 2. 레이저가 격자 안에 있는 동안 무한 시뮬레이션
while 0 <= r < n and 0 <= c < n:
    count += 1 # 거울에 튕기는 횟수 1 증가
    
    # 3. 현재 밟고 있는 거울 모양에 따라 방향 전환
    if grid[r][c] == '/':
        curr_dir = curr_dir ^ 1
    elif grid[r][c] == '\\':
        curr_dir = 3 - curr_dir
        
    # 4. 바뀐 방향으로 한 칸 전진
    r += dr[curr_dir]
    c += dc[curr_dir]

# 레이저가 맵 밖으로 나가면 while문 종료 후 정답 출력
print(count)