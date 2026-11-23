# 1. 구슬은 1초에 한칸씩 이동
# 2. 벽에 부딪히면 반대로 뒤집힘 (1초 소요)
# 3. 1초 이동 후 같은 위치의 구슬이 합쳐짐
#    1) 무게는 합쳐진 구슬의 모든 합
#    2) 방향과 번호는 가장 큰 번호의 방향과 번호
# 4. 격자 안에 남아 있는 구슬의 개수와 가장 무거운 구슬의 무게를 출력

n, m, t = map(int, input().split())

DIR = {
    'U': (-1, 0, 'D'),
    'D': (1, 0, 'U'),
    'L': (0, -1, 'R'),
    'R': (0, 1, 'L')
}

beads = []
for idx in range(1, m + 1):
    r, c, d, w = input().split()
    beads.append([int(r) - 1, int(c) - 1, d, int(w), idx])

for _ in range(t):
    # 1. 1초 이동 (격자 밖이면 방향만 반전, 1초 소모)
    for bead in beads:
        r, c, d, w, num = bead
        
        dr, dc, opp_d = DIR[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            r, c = nr, nc
        else:
            d = opp_d
        
        bead[0], bead[1], bead[2] = r, c, d
    
    # 2. 같은 좌표의 구슬 모으기
    cell_map = {}
    for bead in beads:
        pos = (bead[0], bead[1])
        cell_map.setdefault(pos, []).append(bead)
    
    # 3. 합치기 처리
    next_beads = []
    for pos, group in cell_map.items():
        if len(group) > 1:
            total_w = sum(g[3] for g in group)
            group.sort(key=lambda x: x[4], reverse=True)
            leader = group[0]
            merged = [leader[0], leader[1], leader[2], total_w, leader[4]]
            next_beads.append(merged)
        else:
            next_beads.append(group[0])
    
    beads = next_beads

if not beads:
    print(0, 0)
else:
    max_weight = max(b[3] for b in beads)
    print(len(beads), max_weight)



    
