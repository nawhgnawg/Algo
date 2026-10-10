import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[j].append((i, d))     # j -> i, 길이 d (역방향 그래프)

dist = [float('inf')] * (n + 1)

def dijikstra(start):
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
    
dijikstra(n)

# 1번부터 N번 정점까지의 최단 거리 중 최댓값 구하기
max_dist = 0
for i in range(1, n + 1):
    if dist[i] != float('inf'):
        max_dist = max(max_dist, dist[i])

print(max_dist)