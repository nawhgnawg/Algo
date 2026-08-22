n, m = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(n)]

# 상, 하, 좌, 우, 좌하단 대각선, 좌상단 대각선, 우하단 대각선, 우상단 대각선
dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] != 'L':
            continue
        
        char = grid[i][j]
        
        for k in range(8):
            curr_str = char
            for l in range(1, 3):
                nx = i + dx[k] * l
                ny = j + dy[k] * l
                if 0 <= nx < n and 0 <= ny < m:
                    curr_str += grid[nx][ny]

            if len(curr_str) == 3 and curr_str == 'LEE':
                    answer += 1

print(answer)