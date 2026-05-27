from collections import deque

N, M, K = map(int, input().split())

# 2. 사과 위치 저장 (1-based를 0-based로 변환)
apples = []
for _ in range(M):
    r, c = map(int, input().split())
    apples.append((r - 1, c - 1))

# 3. 명령 저장
commands = []
for _ in range(K):
    d, p = input().split()
    commands.append((d, int(p)))

# 4. 방향 설정 (U, D, R, L)
di = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

# 격자 생성 (빈칸: 0, 사과: 1, 뱀의 몸: 2)
grid = [[0] * N for _ in range(N)]
for r, c in apples:
    grid[r][c] = 1

# 5. 뱀의 초기 상태 설정
snake = deque([(0, 0)]) # 뱀의 몸통 좌표를 담는 큐 (오른쪽이 머리, 왼쪽이 꼬리)
grid[0][0] = 2          # 시작 위치에 뱀(2) 표시
time = 0

# 6. 시뮬레이션 시작
for d, p in commands:
    dx, dy = di[d]

    # p번만큼 해당 방향으로 1칸씩 이동
    for _ in range(p):
        time += 1
        
        # 현재 머리 위치 확인 (큐의 맨 오른쪽)
        curr_x, curr_y = snake[-1]
        nx, ny = curr_x + dx, curr_y + dy


        # 1. 벽 충돌 검사 (벽은 꼬리와 무관하게 즉시 아웃)
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            print(time)
            exit()

        # 2. 사과 여부 확인 및 ★꼬리 먼저 치우기★
        is_apple = (grid[nx][ny] == 1)

        if not is_apple:
            # 사과가 없으므로 꼬리를 당겨서 빈칸(0)으로 만들어 줍니다.
            tail_x, tail_y = snake.popleft()
            grid[tail_x][tail_y] = 0
            
        # 3. 내 몸 충돌 검사
        # (꼬리가 방금 위에서 치워졌으므로, 꼬리 위치로 간 것이라면 grid가 0이 되어 통과함!)
        if grid[nx][ny] == 2:
            print(time)
            exit()
            
        # 4. 머리 전진 반영
        snake.append((nx, ny))
        grid[nx][ny] = 2

# 주어진 명령을 다 수행했는데도 안 부딪혔다면 마지막 시간을 출력
print(time)