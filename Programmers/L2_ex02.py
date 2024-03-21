# 프로그래머스 - 리코쳇 로봇
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]


# 1차
def solution1(board):
    answer = 0
    gx_index, gy_index = 0, 0
    # G(골) 주위에 D(장애물)이 하나도 없으면 멈출 수 없기 때문에 -1을 리턴, 각 모서리에 있으면 멈출 수 있음
    for i, s in enumerate(board):
        if 'G' in s:
            gx_index, gy_index = i, s.index('G')
            if gx_index != 0 or gx_index != len(board[0]) - 1 or gy_index != 0 or gy_index != len(board) - 1:
                None
    return answer

# 2차 - BFS
from collections import deque
def solution2(board):
    answer = -1
    n, m = len(board), len(board[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    q = deque()

    # 시작 위치 찾기
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                sx, sy = x, y
    q.append((sx, sy, 0))

    while q:
        x, y, level = q.popleft()

        if board[x][y] == "G":
            answer = level
            break

        # 한 방향으로 미끄러져 이동
        for dx, dy in direction:
            scope = 1
            while True:
                nx, ny = x + dx * scope, y + dy * scope
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                    if not visited[nx - dx][ny - dy]:
                        visited[nx - dx][ny - dy] = True
                        q.append((nx - dx, ny - dy, level + 1))
                    break
                scope += 1
    return answer



print(solution2(board))