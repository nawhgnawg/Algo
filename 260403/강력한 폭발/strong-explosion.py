n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 폭탄 위치 찾기
bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

# 2. 폭탄 모양 정의 - (dy, dx)
bombs_shape = {1: [(0, 0), (1, 0), (2, 0), (-1, 0), (-2, 0)],   # 세로줄
               2: [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)],   # 십자가
               3: [(0, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]  # X
               } 

# 영역을 계산하는 함수
def calc_area(bombs_types):
    # 폭발을 기록할 배열 N x N
    exploded = [[False] * n for _ in range(n)]
    count = 0

    # 선택한 폭탄 종류에 따라 폭발 시뮬레이션
    for i, (x, y) in enumerate(bombs):
        shape = bombs_shape[bombs_types[i]]
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            # 격자 범위내에 있고, 아직 터지지않았다면
            if 0 <= nx < n and 0 <= ny < n:
                if exploded[nx][ny] == False:
                    exploded[nx][ny] = True
                    count += 1
    return count

# 3. 백트래킹 탐색 함수
def dfs(depth, current_types):
    # 모든 폭탄의 종류를 다 선택했다면, 계산된 영역의 넓이를 반환
    if depth == len(bombs):
        return calc_area(current_types)
    
    max_val = 0
    
    # 1, 2, 3번 폭탄 중 하나를 선택
    for bombs_type in [1, 2, 3]:
        current_types.append(bombs_type)
        # 재귀 호출의 반환값 중 가장 큰 값으로 갱신
        max_val = max(max_val, dfs(depth + 1, current_types))
        current_types.pop()
    
    return max_val

answer = dfs(0, [])
print(answer)