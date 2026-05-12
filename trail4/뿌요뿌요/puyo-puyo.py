from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb_block_count = 0  # 터지는 블럭 수 (크기 >= 4)
max_bomb_size = 0     # 터지든 안 터지든 관계없이 전체 블럭 중 최대 크기

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 방문 여부를 체크할 배열 (전체 탐색 통틀어 단 하나만 관리하면 됩니다)
visited = [[False] * n for _ in range(n)]

# 격자 전체를 순회
for i in range(n):
    for j in range(n):
        # 아직 방문하지 않은 새로운 블럭 덩어리의 시작점 발견!
        if not visited[i][j]:
            target_num = grid[i][j] # 탐색할 블럭의 숫자 고정
            
            # BFS 시작
            q = deque([(i, j)])
            visited[i][j] = True
            current_bomb_size = 0
            
            while q:
                x, y = q.popleft()
                current_bomb_size += 1 # 큐에서 꺼낼 때마다 크기 증가
                
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        # 같은 숫자이면서 아직 방문하지 않은 인접한 칸인 경우
                        if grid[nx][ny] == target_num and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            
            # 1. 터지는 블럭 조건 검사 (크기가 4 이상인 경우만 카운트)
            if current_bomb_size >= 4:
                bomb_block_count += 1
                
            # 2. 최대 블럭 크기 갱신 (★ 크기 상관없이 모든 덩어리 중 최댓값 유지)
            max_bomb_size = max(max_bomb_size, current_bomb_size)

print(bomb_block_count, max_bomb_size)