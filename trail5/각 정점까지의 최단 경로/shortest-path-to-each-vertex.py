import heapq

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    # 무방향 그래프이므로 양쪽 방향 모두 추가
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [float('inf')] * (n + 1)

def dijkstra(start):
    pq = []
    # (거리, 노드)를 튜플로 저장
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

dijkstra(k)

for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])

