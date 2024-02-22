# 프로그래머스 - 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 이어진 뭉탱이 찾기 -> BFS/DFS
n = 3   # 컴퓨터의 개수
computers = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]   # 연결에 대한 정보

# 1차
def solution1(n, computers):
    answer = 0
    nodes = [[] * n for _ in range(len(computers))]

    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1:
                nodes[i].append(j)
        nodes[i].remove(i)

    return answer

# 2차 - DFS
def solution2(n, computers):

    def dfs(v):
        visited[v] = True

        for nei in range(n):    # 인접 노드 탐구
            if not visited[nei] and computers[v][nei]:  # unvisited + 인접할 때
                dfs(nei)

    count = 0
    visited = [False] * n

    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1

    return count


# 3차 - BFS
from collections import deque
def solution3(n, computers):

    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    q.append(a)

    answer = 0
    visited = [0 for _ in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer

print(solution3(n, computers))