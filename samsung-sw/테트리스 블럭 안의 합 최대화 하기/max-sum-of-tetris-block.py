n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

max_sum = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 'ㅗ' 모양을 제외한 4가지 블록 탐색 (DFS 깊이 4)
def dfs(x, y, depth, current_sum):
    global max_sum
    
    # 4칸을 모두 모았으면 최댓값 갱신 후 종료
    if depth == 4:
        max_sum = max(max_sum, current_sum)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, current_sum + grid[nx][ny])
            visited[nx][ny] = False  # 백트래킹 (원상복구)

# 2. 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 별도 처리
def check_exotic_shape(x, y):
    global max_sum
    
    # 현재 위치 (x, y)를 중심점으로 삼고 주변 4방향 값을 모음
    neighbors = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            neighbors.append(grid[nx][ny])
    
    # 주변 칸이 3개 미만이면 'ㅗ' 계열을 만들 수 없음
    if len(neighbors) < 3:
        return
    
    # 주변 칸이 3개면 그 3개를 다 더함 ('ㅗ', 'ㅜ' 등)
    # 주변 칸이 4개면 그 중 가장 작은 하나를 빼고 3개를 더함 (4가지 중 최댓값)
    if len(neighbors) == 3:
        max_sum = max(max_sum, grid[x][y] + sum(neighbors))
    elif len(neighbors) == 4:
        max_sum = max(max_sum, grid[x][y] + sum(neighbors) - min(neighbors))


for i in range(n):
    for j in range(m): 
        # DFS 시작
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = False

        # 'ㅗ' 모양 체크
        check_exotic_shape(i, j)

print(max_sum)