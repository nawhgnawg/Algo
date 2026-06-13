from collections import deque

N, r, c, d = map(int, input().split())
r -= 1
c -= 1
d -= 1

# 입력 방향을 내부 표현으로 변환합니다.
# 입력(0-indexed): 0=상, 1=하, 2=좌, 3=우
# 내부(반시계):    0=상, 1=좌, 2=하, 3=우
dir_map = [0, 2, 1, 3]
d = dir_map[d]

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

# 반시계 방향: 상(0), 좌(1), 하(2), 우(3)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


# (r, c)가 격자 범위 내인지 확인합니다.
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


# (sr, sc)에서 출발하는 BFS를 수행하여
# 모든 바다 칸까지의 최단 거리를 반환합니다.
# 도달 불가능한 칸은 -1로 표시합니다.
def bfs(sr, sc):
    dist = [[-1] * N for _ in range(N)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if in_range(nr, nc) and grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[cr][cc] + 1
                q.append((nr, nc))
    return dist


# 1단계: 현재 위치와 방향에서 우선순위에 따라
# 이동할 다음 칸을 반환합니다.
# 이동 가능한 칸이 없으면 (-1, -1, -1)을 반환합니다.
def get_next(r, c, d):
    for delta in [0, 1, -1, 2]:
        nd = (d + delta + 4) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        if in_range(nr, nc) and grid[nr][nc] == 0 and not visited[nr][nc]:
            return nr, nc, nd
    return -1, -1, -1


# 바다 칸의 총 개수를 셉니다.
total = sum(grid[i][j] == 0 for i in range(N) for j in range(N))

# 시작 위치를 방문 처리하고 출력합니다.
visited[r][c] = True
print(r + 1, c + 1)
cnt = 1

while cnt < total:
    # 1단계: 인접 탐험
    # 우선순위에 따라 이동 가능한 칸이 없을 때까지 반복합니다.
    while True:
        nr, nc, nd = get_next(r, c, d)
        if nr == -1:
            break
        r, c, d = nr, nc, nd
        visited[r][c] = True
        cnt += 1
        print(r + 1, c + 1)

    if cnt >= total:
        break

    # 2단계: 가장 가까운 미방문 바다 찾기
    # 현재 위치에서 BFS를 수행하여 거리맵을 구합니다.
    dist_from = bfs(r, c)

    # 미방문 바다 칸 중 최소 거리인 칸을 선택합니다.
    # 행-열 순서로 순회하므로 거리만 비교하면 됩니다.
    tr, tc, min_dist = -1, -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 or visited[i][j] or dist_from[i][j] == -1:
                continue
            if min_dist == -1 or dist_from[i][j] < min_dist:
                tr, tc, min_dist = i, j, dist_from[i][j]

    # 목표 칸에서 BFS를 수행하여
    # 경로 추적에 필요한 거리맵을 구합니다.
    dist_to = bfs(tr, tc)

    # 매 단계 목표까지의 거리가 1 줄어드는 방향 중
    # 좌, 하, 우, 상 순서로 우선순위가 높은 쪽을 선택합니다.
    while r != tr or c != tc:
        for ndir in [1, 2, 3, 0]:
            nr, nc = r + dr[ndir], c + dc[ndir]
            if in_range(nr, nc) and grid[nr][nc] == 0 and dist_to[nr][nc] == dist_to[r][c] - 1:
                r, c, d = nr, nc, ndir
                break

    # 목표 칸을 방문 처리하고 출력합니다.
    visited[r][c] = True
    cnt += 1
    print(r + 1, c + 1)
