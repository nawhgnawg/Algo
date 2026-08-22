n, m = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(n)]

# 상, 하, 좌, 우, 좌하단 대각선, 좌상단 대각선, 우하단 대각선, 우상단 대각선
dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

answer = 0

for i in range(n):
    for j in range(m):
        # 'L'로 시작하지 않으면 패스!
        if grid[i][j] != 'L':
            continue
        
        # 8가지 방향을 모두 찔러봅니다.
        for k in range(8):
            curr_str = 'L'
            for l in range(1, 3):
                nx = i + dx[k] * l
                ny = j + dy[k] * l
                # 범위 체크
                if 0 <= nx < n and 0 <= ny < m:
                    curr_str += grid[nx][ny]
                else:
                    break   # 격자를 벗어나면 더 이상 글자를 안 붙이고 멈춤

            # 조립된 3글자가 'LEE'라면 정답 카운트!
            if len(curr_str) == 3 and curr_str == 'LEE':
                    answer += 1

print(answer)