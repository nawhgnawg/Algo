n, m, t = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 살아있는 구슬들의 좌표 리스트 (0-indexed로 변환)
beads = []
for _ in range(m):
    r, c = map(int, input().split())
    beads.append((r - 1, c - 1))

# 상, 하, 좌, 우 우선순위 방향 벡터
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# T초 동안 시뮬레이션 반복
for _ in range(t):
    if not beads:
        break

    # 각 위치로 이동하는 구슬의 개수를 기록할 2차원 배열
    pos_count = [[0] * n for _ in range(n)]

    # 1. 모든 구슬이 동시에 다음 위치 계산
    for r, c in beads:
        max_val = -1
        next_r, next_c = r, c

        # 상, 하, 좌, 우 순서로 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 격자 범위 내에 있는지 확인
            if 0 <= nr < n and 0 <= nc < n:
                # 값이 더 큰 경우에만 갱신 (같을 경우 먼저 탐색된 상/하/좌/우 우선순위 유지)
                if grid[nr][nc] > max_val:
                    max_val = grid[nr][nc]
                    next_r, next_c = nr, nc
        
        # 이동할 위치에 구슬 카운트 증가
        pos_count[next_r][next_c] += 1

        # 2. 충돌 처리: 도착한 구슬이 정확히 1개인 경우에만 생존
        new_beads = []
        for r in range(n):
            for c in range(n):
                if pos_count[r][c] == 1:
                    new_beads.append((r, c))

        beads = new_beads

# 최종 남아 있는 구슬의 수 출력
print(len(beads))
