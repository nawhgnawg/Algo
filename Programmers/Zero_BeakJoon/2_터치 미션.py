# 2. 터치 미션

# 참가자가 두 가지 기술 중 하나를 사전에 사용할 수 있는 상황에서, 결과적으로 터치 미션을 클리어하는 최소 시간을 반환한다.
# 어떻게 하더라도 도달할 수 있는 타겟 지점이 없어 클리어할 수 없는 경우에는 -1을 반환한다.

from collections import deque


def bfs(n, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    dist = [[-1] * n for _ in range(n)]  # 아직 방문 안함 -> -1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "P":
                q.append((i, j))
                dist[i][j] = 0

    while q:
        r, c = q.popleft()
        for k in range(4):
            nx = r + dx[k]
            ny = c + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != 'X':
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = dist[r][c] + 1
                        q.append((nx, ny))

    max_num = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'O':
                if max_num < dist[i][j]:
                    max_num = dist[i][j]
    return max_num


def solution(n, board):
    answer = -1
    # 특정 타겟 제거
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'O':
                a = [[''] * n for _ in range(n)]
                for l1 in range(n):
                    for l2 in range(n):
                        a[l1][l2] = board[l1][l2]
                        if l1 == i and l2 == j:
                            a[l1][l2] = 'B'
                cur = bfs(n, a)
                if cur != -1:
                    if answer == -1 or answer > cur:
                        answer = cur

    # 벽 제거
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                a = [[''] * n for _ in range(n)]
                for l1 in range(n):
                    for l2 in range(n):
                        a[l1][l2] = board[l1][l2]
                        if l1 == i and l2 == j:
                            a[l1][l2] = 'B'

                cur = bfs(n, a)
                if cur != -1:
                    if answer == -1 or answer > cur:
                        answer = cur

    return answer


# return 4
n, board = 6, [["B", "O", "B", "B", "B", "B"],
               ["X", "X", "X", "X", "X", "B"],
               ["B", "B", "O", "B", "P", "B"],
               ["X", "X", "B", "X", "B", "B"],
               ["B", "B", "O", "X", "B", "B"],
               ["B", "B", "B", "B", "B", "B"]]
# # return -1
# n, board = 6, [["P", "B", "B", "B", "B", "B"],
#                ["B", "B", "B", "B", "B", "B"],
#                ["B", "B", "X", "X", "X", "X"],
#                ["B", "B", "X", "X", "X", "X"],
#                ["B", "B", "X", "X", "X", "O"],
#                ["B", "B", "X", "X", "O", "O"]]
# # return 11
# n, board = 6, [["P", "B", "B", "B", "B", "B"],
#                ["B", "B", "B", "B", "B", "B"],
#                ["B", "B", "X", "X", "X", "X"],
#                ["B", "B", "X", "X", "X", "X"],
#                ["B", "B", "X", "X", "X", "O"],
#                ["B", "B", "X", "B", "O", "O"]]
print(solution(n, board))
