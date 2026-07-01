n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for r in range(n):
    for c in range(n):
        count = 0
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    count += 1
        
        if count >= 3:
            answer += 1

print(answer)
