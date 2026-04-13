n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# 이동 방향 (우상단, 좌상단, 좌하단, 우하단)
dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

def rec_sum(r, c, w, h):
    # 직사각형은 마주보는 변의 길이가 같기때문에
    # 우상단으로 w 칸, 좌상단으로 h 칸, 좌하단으로 w 칸, 우하단으로 h 칸 이동
    move_count = [w, h, w, h]

    current_sum = 0
    x, y = r, c

    # 4개의 방향을 순서대로 돌면서 
    for i in range(4):
        # 각 방향에 정해둔 이동 횟수만큼 전진한다.
        for _ in range(move_count[i]):
            x += dx[i]
            y += dy[i]
            # 이동도중 격자를 벗어나면 무효처리 0 반환
            if not (0 <= x < n and 0 <= y < n):
                return 0

            current_sum += grid[x][y]

    return current_sum

max_score = 0

for r in range(n):
    for c in range(n):
        # 해당 꼭짓점에서 뻗어나갈 수 있는 모든 너비와 높이를 대입한다.
        # 격자 크기가 n 이면, 길이는 1 ~ n - 1 까지만 가능하다.
        for w in range(1, n):
            for h in range(1, n):
                current_sum = rec_sum(r, c, w, h)
                max_score = max(max_score, current_sum)

print(max_score)