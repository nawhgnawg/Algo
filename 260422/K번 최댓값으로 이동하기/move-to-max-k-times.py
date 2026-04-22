from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 현재 위치
curr_r, curr_c = r - 1, c - 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# K번 이동 시도 
for _ in range(k):
    # 갈 수 있는 칸 확인
    visited = [[False] * n for _ in range(n)]

    q = deque([(curr_r, curr_c)])
    visited[curr_r][curr_c] = True

    start_num = grid[curr_r][curr_c]
    candidates = []     # 갈 수 있는 칸을 담을 리스트

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 + 조건 체크
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] < start_num:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    candidates.append((grid[nx][ny], nx, ny))
    
    # 더 이상 갈 곳이 없으면 종료
    if not candidates:
        break
    
    # 우선 순위에 따라 정렬
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))

    # 최우선 후보로 현재 위치 업데이트
    _, curr_r, curr_c = candidates[0]

print(curr_r + 1, curr_c + 1)
