n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 가능한 기준점 찾기 - grid[0][0] ~ grid[n - 3][n - 3]
max_total = 0


for i in range(n - 2):
    for j in range(n - 2):
        total = 0

        for r in range(i, i + 3):
            for c in range(j, j + 3):
                total += grid[r][c]
        
        max_total = max(total, max_total)

print(max_total)
