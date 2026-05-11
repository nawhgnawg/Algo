from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

# DFS
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return True

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False

if dfs(0, 0):
    print(1)
else:
    print(0)

# BFS
# q = deque([(0, 0)])
# visited = [[False] * m for _ in range(n)]
# visited[0][0] = True

# ans = 0
# while q:
#     x, y = q.popleft()

#     if x == n - 1 and y == m - 1:
#         ans = 1
#         break

#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 0:
#             visited[nx][ny] = True
#             q.append((nx, ny))

# print(ans)