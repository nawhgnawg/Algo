# 프로그래머스 Level 3 - 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 거리 배열 (-1은 아직 방문 안 함을 의미)
    distance = [-1] * (n + 1)
    distance[1] = 0  # 시작 노드(1)의 거리는 0
    print(graph)
    print(distance)
    queue = deque([1])
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if distance[next_node] == -1:  # 아직 방문 안 한 노드
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # 최대 거리
    max_dist = max(distance)
    return distance.count(max_dist)

n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]       # return 3
print(solution(n, edge))
