n, m, r, c = map(int, input().split())
directions = list(input().split())

grid = [[0] * n for i in range(n)]

r -= 1
c -= 1

di = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

# 1. 주사위 6면의 초기 상태 세팅 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
up, down, front, back, left, right = 1, 6, 2, 5, 4, 3


curr_x, curr_y = r, c
grid[curr_x][curr_y] = down

for d in directions:
    nx = curr_x + di[d][0]
    ny = curr_y + di[d][1]

    # 격자 밖으로 벗어나면 다음과정 수행
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

    # 이동 확정
    curr_x, curr_y = nx, ny

    # 주사위 굴리기 (방향에 따라 4개의 면이 서로 자리를 바꿈)
    if d == 'R':
        up, right, down, left = left, up, right, down
    elif d == 'L':
        up, left, down, right = right, up, left, down
    elif d == 'U':
        up, back, down, front = front, up, back, down
    elif d == 'D':
        up, front, down, back = back, up, front, down
    
    # 이동한 칸에 새로운 아랫면 칠하기
    grid[curr_x][curr_y] = down

answer = sum(sum(row) for row in grid)
print(answer)

    
