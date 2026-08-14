r, c = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(r)]

answer = 0

# 첫 번째 도착지 (i, j)
for i in range(1, r - 1):
    for j in range(1, c - 1):
        
        # 두 번째 도착지 (k, l)
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                # 색깔이 번갈아 나오는지 확인
                if grid[0][0] != grid[i][j] and grid[i][j] != grid[k][l] and grid[k][l] != grid[r - 1][c - 1]:
                   answer += 1

print(answer)
            