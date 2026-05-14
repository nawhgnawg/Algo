n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

r -= 1
c -= 1

bomb = grid[r][c]
grid[r][c] = 0


# 1. 십자 모양 폭발 터트리기
for i in range(4):
    for j in range(1, bomb):
        nx = r + (dx[i] * j)
        ny = c + (dy[i] * j)

        # 격자 범위 내에 있다면 0으로 비움 (폭파)
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 0:
            grid[nx][ny] = 0

# 2. 중력(떨어뜨리기) 구현
# ⭐️ 각 열(세로줄)을 기준으로 반복
for j in range(n):
    # 해당 열에서 터지지 않고 살아남은 숫자(0이 아닌 수)만 위에서부터 순서대로 추출
    temp = [grid[i][j] for i in range(n) if grid[i][j] != 0]
    
    # 격자 크기(n)에서 남은 블럭 수를 빼면 채워야 할 빈칸(0)의 개수가 나옴
    temp = [0] * (n - len(temp)) + temp
    
    # 완성된 1차원 배열(temp)을 다시 원래 격자의 열에 순서대로 덮어씌움
    for i in range(n):
        grid[i][j] = temp[i]

for row in grid:
    print(*(row))
        
