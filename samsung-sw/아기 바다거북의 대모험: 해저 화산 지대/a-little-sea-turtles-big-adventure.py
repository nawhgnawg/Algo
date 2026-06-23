from collections import deque

N, M, K = map(int, input().split())
# 바다의 정보
grid = [list(map(int, input().split())) for _ in range(N)]

# 바다거북 상태 관리
# is_dead: 화석화 여부, is_arrived: 안식처 도착 여부, arrival_time: 도착 턴
turtles = [{'r': 0, 'c': 0, 'is_dead': False, 'is_arrived': False, 'arrival_time': -1} for _ in range(M + 1)]
for i in range(1, M + 1):
    r, c = map(int, input().split())
    turtles[i]['r'], turtles[i]['c'] = r, c
    
# 해저 화산 상태 관리
vols = []
volcano_map = [[-1] * N for _ in range(N)]
for i in range(K):
    r, c, P = map(int, input().split())
    vols.append({'r': r, 'c': c, 'P': P, 'pressure': 0})
    volcano_map[r][c] = i
    
fossil_grid = [[False] * N for _ in range(N)]

# 1. 문제의 우선순위: 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 최단 경로 탐색 함수 (BFS)
def get_next_step(tr, tc, living_turtles):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    visited[tr][tc] = True
    
    # 첫 번째 스텝만 따로 큐에 넣어 방향(first_dir)을 기억하도록 함
    for i in range(4):
        nr, nc = tr + dr[i], tc + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] != 1 and not fossil_grid[nr][nc] and (nr, nc) not in living_turtles:
                visited[nr][nc] = True
                q.append((nr, nc, i))
                # 바로 안식처라면 즉시 해당 방향 리턴
                if nr == N - 1 and nc == N - 1:
                    return i
                    
    while q:
        r, c, first_dir = q.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if grid[nr][nc] != 1 and not fossil_grid[nr][nc] and (nr, nc) not in living_turtles:
                        visited[nr][nc] = True
                        q.append((nr, nc, first_dir))
                        # 가장 먼저 (N-1, N-1)을 밟는 브랜치의 첫 방향이 무조건 1순위 최단경로임
                        if nr == N - 1 and nc == N - 1:
                            return first_dir
    return -1 # 경로가 없으면 -1 리턴

# 최대 100턴 동안 시뮬레이션 진행
for turn in range(1, 101):
    
    # 1단계: 바다거북 이동
    for i in range(1, M + 1):
        if turtles[i]['is_dead'] or turtles[i]['is_arrived']:
            continue
        
        # 다른 '살아있는' 거북이들의 위치를 장애물로 기록
        living_turtles = set()
        for j in range(1, M + 1):
            if i != j and not turtles[j]['is_dead'] and not turtles[j]['is_arrived']:
                living_turtles.add((turtles[j]['r'], turtles[j]['c']))
                
        next_dir = get_next_step(turtles[i]['r'], turtles[i]['c'], living_turtles)
        
        if next_dir != -1: # 갈 수 있는 최단 경로가 있다면
            turtles[i]['r'] += dr[next_dir]
            turtles[i]['c'] += dc[next_dir]
            
            # 안식처에 도착했다면 즉시 맵에서 제외
            if turtles[i]['r'] == N - 1 and turtles[i]['c'] == N - 1:
                turtles[i]['is_arrived'] = True
                turtles[i]['arrival_time'] = turn
                
    # 2단계: 모든 화산 마그마 압력 10 증가
    for v in range(K):
        vols[v]['pressure'] += 10
        
    # 3단계: 화산 분출 및 연쇄 반응
    erupted_this_turn = [False] * K
    heat_grid = [[0] * N for _ in range(N)] # 이번 턴의 누적 열기 기록 맵
    q = deque()
    
    for v in range(K):
        if vols[v]['pressure'] >= vols[v]['P']:
            erupted_this_turn[v] = True
            q.append(v)
            
    while q:
        v_idx = q.popleft()
        v = vols[v_idx]
        r, c = v['r'], v['c']
        P = v['P']
        
        heat_grid[r][c] += P # 분출지점 열기 폭발
        
        # 4방향으로 열기 전파
        for i in range(4):
            curr_heat = P
            curr_r, curr_c = r, c
            while True:
                curr_r += dr[i]
                curr_c += dc[i]
                curr_heat //= 2 # 절반으로 감소 (소수점 내림)
                
                if curr_heat == 0: break
                if not (0 <= curr_r < N and 0 <= curr_c < N): break
                if grid[curr_r][curr_c] == 1: break # 산호초는 열기를 막음 (거북이나 화석은 막지 못함)
                
                heat_grid[curr_r][curr_c] += curr_heat # 열기 누적
                
                # 연쇄 반응 체크: 현재 도달한 곳에 아직 안 터진 화산이 있다면?
                v_target = volcano_map[curr_r][curr_c]
                if v_target != -1 and not erupted_this_turn[v_target]:
                    # 내부 압력 + 외부 누적 열기가 임계치 이상이면 연쇄 폭발
                    if vols[v_target]['pressure'] + heat_grid[curr_r][curr_c] >= vols[v_target]['P']:
                        erupted_this_turn[v_target] = True
                        q.append(v_target)
                        
    # 거북이 위기 (화석화) 검사
    for i in range(1, M + 1):
        if not turtles[i]['is_dead'] and not turtles[i]['is_arrived']:
            tr, tc = turtles[i]['r'], turtles[i]['c']
            if heat_grid[tr][tc] >= 20: # 서있는 칸의 누적 열기가 20 이상이면 즉사
                turtles[i]['is_dead'] = True
                fossil_grid[tr][tc] = True # 영구 화석(장애물) 등록
                
    # 4단계: 환경 초기화
    for v in range(K):
        if erupted_this_turn[v]:
            vols[v]['pressure'] = 0 # 이번 턴에 터진 화산들만 압력 0으로 리셋
            
    # (최적화) 모든 거북이가 도착했거나 죽었다면 더 이상 시뮬레이션을 진행할 필요가 없음
    all_done = True
    for i in range(1, M + 1):
        if not turtles[i]['is_dead'] and not turtles[i]['is_arrived']:
            all_done = False
            break
    if all_done:
        break
        
# 최종 결과 출력: 각 거북이의 도착 턴 (도착 못했거나 죽었다면 초기값인 -1이 출력됨)
for i in range(1, M + 1):
    print(turtles[i]['arrival_time'])