import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)
path = [0] * (n + 1)  # 직전 부모 노드를 기록할 배열

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

A, B = map(int, input().split())

def dijkstra(start):
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
                path[next_node] = cur  # 직전 방문 노드 기록
                heapq.heappush(pq, (cost, next_node))

dijkstra(A)

# 1. 최단 거리 출력
print(dist[B])
                
# 2. 경로 역추적 (B부터 A까지 거슬러 올라감)
route = []
curr = B
while curr != 0:
    route.append(curr)
    curr = path[curr]

# A부터 B 순서가 되도록 반전 후 출력
route.reverse()
print(*route)