# 1. 벽에 부딪혀 방향을 바꿀 때는 시간이 안든다.
# 2. 같은 칸에 구슬이 k개 이하면 다음과정, 
#    k를 넘는다면 구슬의 속도가 빠른(+ 구슬의 번호가 더 큰) 구슬 k개만 살아남음

n, m, t, k = map(int, input().split())

DIR = {
    'L': (0, -1, 'R'),
    'R': (0, 1, 'L'),
    'U': (-1, 0, 'D'),
    'D': (1, 0, 'U')
}

# 각 구슬: [r, c, d, v, num] (0-indexed 좌표, 1-indexed 번호)
beads = []
for idx in range(1, m + 1):
    r, c, d, v = input().split()
    beads.append([int(r) - 1, int(c) - 1, d, int(v), idx])

for _ in range(t):
    # 1. 모든 구슬을 각자의 속도 v만큼 이동
    for bead in beads:
        r, c, d, v, _ = bead
        for _ in range(v):
            dr, dc, opp_d = DIR[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                r, c = nr, nc
            else:
                d = opp_d
                ndr, ndc, _ = DIR[d]
                r, c = r + ndr, c + ndc
        bead[0], bead[1], bead[2] = r, c, d

    # 2. 같은 좌표 (r, c)에 모인 구슬들을 그룹화해 k개만 생존
    cell_map = {}
    for bead in beads:
        pos = (bead[0], bead[1])
        cell_map.setdefault(pos, []).append(bead)

    next_beads = []
    for pos, group in cell_map.items():
        if len(group) > k:
            # 속도(v) 내림차순, 같다면 번호(num) 내림차순 정렬
            group.sort(key=lambda x: (x[3], x[4]), reverse=True)
            group = group[:k]
        next_beads.extend(group)

    beads = next_beads

print(len(beads))

# for _ in range(t):
#     for r in range(n):
#         for c in range(n):
#             if beads[r][c] == 0:
#                 continue
            
#             # 구슬 정보
#             bead_v, num, count = beads[r][c]

#             d, v = grid[r][c]
#             curr_r, curr_c = r, c   # 시작 위치
#             for i in range(v):
#                 dr, dc, next_d = DIR[d]
#                 nr, nc = curr_r + dr, curr_c + dc
#                 # 범위 내에 있으면 최종 위치 카운트
#                 if 0 <= nr < n and 0 <= nc < n:
#                     curr_r, curr_c = nr, nc
#                 # 범위 밖에 있으면 반대방향으로 바꾸고 이동
#                 else:
#                     d = next_d
#                     dr, dc, next_d = DIR[d]
#                     nr, nc = curr_r + dr, curr_c + dc

#             # 구슬 이동
#             beads[r][c]
#             beads[curr_r][curr_c]

#             # 구슬 수 확인 후 처리
#             for r in range(n):
#                 for c in range(n):
#                     if beads[r][c] > k:
                        



