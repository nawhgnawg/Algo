import heapq

n, m = map(int, input().split())
a, b, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue

        for next_node, weight in graph[cur]:
            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return dist

# a, b, c 3개 정점에서 출발하는 다익스트라 수행
dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_c = dijkstra(c)

answer = 0
for i in range(1, n + 1):
    # a, b, c 정점 자체는 제외
    if i in (a, b, c):
        continue

    # a, b, c 중 가장 가까운 거리를 선택
    min_dist = min(dist_a[i], dist_b[i], dist_c[i])

    if min_dist != float('inf'):
        answer = max(answer, min_dist)

print(answer)


# 시간 초과 발생
# answer = 0
# for i in range(1, n + 1):
#     if i == a or i == b or i == c:
#         continue

#     dist = [float('inf')] * (n + 1)
#     dijkstra(i)

#     min_dist = float('inf')
#     for j in [a, b, c]:
#         if dist[j] == float('inf'):
#             continue
#         elif dist[j] < min_dist:
#             min_dist = dist[j]

#     answer = max(min_dist, answer)

# print(answer)
