from collections import deque

n, m, r, c = map(int, input().split())

# 좌표
grid = [[0] * n for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 인덱스 정렬
r -= 1
c -= 1

# 초기 폭탄 위치
grid[r][c] = 1

q = deque([(r, c)])

# m초 후 
for t in range(1, m + 1):

    dist = 2 ** (t - 1)

    # 새로 생길 폭탄의 위치를 담을 임시 리스트
    # (격자를 순회하는 도중에 바로 grid에 1을 찍어버리면, 방금 생긴 폭탄이 이번 턴에 또 터지는 버그가 생길 수 있음)
    new_bombs = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                # 2. 기존 폭탄(i, j)에서 4방향으로 퍼질 새로운 폭탄 위치 계산
                for k in range(4):
                    nx = i + (dx[k] * dist)
                    ny = j + (dy[k] * dist)

                    # 격자 안에 있고, 아직 폭탄이 없는 빈 공간이라면
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        new_bombs.append((nx, ny))
    
    # 3. 이번 턴에 새로 생긴 폭탄들을 격자에 한 번에 반영합니다.
    for nx, ny in new_bombs:
        grid[nx][ny] = 1

print(sum(sum(row) for row in grid))

