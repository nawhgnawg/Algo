import sys
grid = [list(map(int, input().split())) for _ in range(19)]

# 오른쪽, 아래, 우하단 대각선, 우상단 대각선
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if grid[i][j] == 0:
            continue
    
        c = grid[i][j]
        # 4가지 방향 체크
        for k in range(4):
            cnt = 1
            for l in range(1, 5):
                nx = i + dx[k] * l
                ny = j + dy[k] * l

                if 0 <= nx < 19 and 0 <= ny < 19 and grid[nx][ny] == c:
                    cnt += 1
                else:
                    break

            # 오목이면 육목인지 검사
            if cnt == 5:
                # 시작점의 바로 '이전' 돌의 위치
                prev_x = i - dx[k]
                prev_y = j - dy[k]
                # 5개가 끝난 '다음(6번째)' 돌의 위치
                next_x = i + dx[k] * 5
                next_y = j + dy[k] * 5

                # 이전 돌이 같은 색이면 육목이므로 패스
                if 0 <= prev_x < 19 and 0 <= prev_y < 19 and grid[prev_x][prev_y] == c:
                    continue

                # 다음 돌이 같은 색이어도 육목이므로 패스
                if 0 <= next_x < 19 and 0 <= next_y < 19 and grid[next_x][next_y] == c:
                    continue

                # 완벽한 5목
                print(c)
                print(i + dx[k] * 2 + 1, j + dy[k] * 2 + 1)
                exit()

print(0)