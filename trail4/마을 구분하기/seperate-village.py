n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 나 자신을 방문했으므로 기본 크기는 1
    people_count = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                # 이웃 칸으로부터 연결된 사람 수를 재귀적으로 받아와서 누적합
                people_count += dfs(nx, ny)
    
    return people_count

# 각 마을의 사람 수를 저장할 리스트
town_sizes = []

for i in range(n):
    for j in range(n):
        # 새로운 마을의 시작점 발견!
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            # 탐색을 시작하여 해당 마을의 총 사람 수를 구해 리스트에 추가
            town_sizes.append(dfs(i, j))


town_sizes.sort()

print(len(town_sizes)) # 총 마을의 수
for size in town_sizes:
    print(size)