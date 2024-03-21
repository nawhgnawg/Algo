# 프로그래머스 - 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 기본적인 탐색 문제. BFS/DFS 상관 없음

maps = ["X591X","X1X5X","X231X", "1XXX1"]

# 1차
# 아무 섬도 없으면 -1 return
def solution(maps):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                period = 0
                q = [(i, j)]

                while q:
                    x, y = q.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    period += int(maps[x][y])

                    # 주위에 붙어 있는 숫자가 있는지 확인
                    for k in range(4):
                        ax, ay = x + dx[k], y + dy[k]
                        if ax > -1 and ax < n and ay > -1 and ay < m and maps[ax][ay] != 'X' and not visited[ax][ay]:
                            q.append((ax, ay))
                answer.append(period)
    return sorted(answer) if answer else [-1]

print(solution(maps))