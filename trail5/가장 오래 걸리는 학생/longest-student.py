import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
    graph[j].append((i, d))

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

dist_n = dijkstra(n)

answer = 0
for i in range(1, n + 1):
    if dist_n[i] != float('inf'):
        answer = max(dist_n[i], answer)

print(answer)

