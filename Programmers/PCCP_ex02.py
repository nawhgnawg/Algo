# PCCP 기출문제 2번 석유 시추
# https://school.programmers.co.kr/learn/courses/19344/lessons/242259

land = [[0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1]]

result = 9

from collections import deque

def solution(land):
    n, m = len(land), len(land[0])  # 행(n), 열(m) 크기
    visited = [[False] * m for _ in range(n)]
    max_oil = 0  # 최대 석유량

    # 4방향 (상, 하, 좌, 우) 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        oil_size = 0
        cols = set()  # 현재 석유 덩어리가 포함된 열(중복 방지)

        while queue:
            x, y = queue.popleft()
            oil_size += 1
            cols.add(y)  # 현재 석유가 속한 열 추가

            # 4방향 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        # 같은 열에 속한 모든 석유의 크기를 같게 설정
        total_oil = oil_size * len(cols)
        return total_oil

    # 전체 탐색 (각 석유 덩어리를 찾기)
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                max_oil = max(max_oil, bfs(i, j))

    return max_oil


print(solution(land).__eq__(result))
