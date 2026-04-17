from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 1. 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2. 방문 배열
visited = [[0] * m for _ in range(n)]

# 큐 생성
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위랑 조건(뱀이 없는 곳)을 만족하는지 확인 
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
            # 방문하지 않았다면 큐에 추가
            if not visited[nx][ny]:
                q.append((nx, ny))

print(visited[n - 1][m - 1])