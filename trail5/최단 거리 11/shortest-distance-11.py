import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

A, B = map(int, input().split())

dist = [float('inf')] * (n + 1)

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, weight in graph[cur]:
            cost = weight + d
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

# B를 시작점으로 실행
dijkstra(B)

# 1. 최단 거리 출력
print(dist[A])

# 2. A부터 시작해서 사전순으로 가장 작은 경로 추적
path = [A]
cur = A

while cur != B:
    # 다음으로 갈 수 있는 최단 경로 후보 중 번호가 가장 작은 정점 선택
    next_candidates = []
    for next_node, weight in graph[cur]:
        if dist[cur] == dist[next_node] + weight:
            next_candidates.append(next_node)

    # 사전순으로 앞서는 가장 작은 정점 번호 선택
    next_node = min(next_candidates)
    path.append(next_node)
    cur = next_node

print(*path)


