from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]



time = 0
last_melt_size = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 전체 빙하의 개수를 미리 세기
count = sum([row.count(1) for row in a])

# 빙하가 모두 녹을 때까지 반복
while count > 0:
    time += 1
    # 바깥쪽 물을 탐색하기 위한 BFS

    q = deque()
    visited = [[False] * m for _ in range(n)]

    found = False
    for r in range(n):
        for c in range(n):
            if a[r][c] == 0:
                q.append((r, c))
                visited[r][c] = True
                found = True
                break
        if found:
            break
    
    # 이번 초에 녹을 빙하의 위치
    melt_targets = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 안에 들어오고 방문 안하고 물이여야함
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if a[nx][ny] == 0:
                    # 물이면 계속 탐색
                    q.append((nx, ny))
                elif a[nx][ny] == 1:
                    # 빙하를 만나면 녹을 대상으로 기록하고 더 이상 전진하지 않음
                    melt_targets.append((nx, ny))
    
    # 이번초에 녹는 빙하의 수를 갱신
    last_melt_size = len(melt_targets)

    # 실제로 빙하를 녹이고 카운트 삭제
    for r, c in melt_targets:
        a[r][c] = 0
        count -= 1

print(time, last_melt_size)
        


