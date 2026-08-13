n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

for i in range(n):
    for j in range(n - 2):
        curr_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_sum = max(curr_sum, max_sum)

        if max_sum == 3:
            break

print(max_sum)