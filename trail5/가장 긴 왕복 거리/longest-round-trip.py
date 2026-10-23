import heapq

n, m, x = map(int, input().split())

# 정방향 그래프: u -> v
graph = [[] for _ in range(n + 1)]
# 역방향 그래프: v -> u (간선 방향이 뒤집힌 형태)
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    rev_graph[v].append((u, w))

def dijkstra(start, g):
    dist = [float('inf')] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, weight in g[cur]:
            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return dist

# 1. X에서 각 정점으로 가는 최단 거리 (정방향 그래프 사용)
# 결과: X -> i
dist_from_x = dijkstra(x, graph)

# 2. 각 정점에서 X로 가는 최단 거리 (역방향 그래프 사용)
# 결과: i -> X
dist_to_x = dijkstra(x, rev_graph)

# 3. 모든 정점에 대해 (i -> X) + (X -> i) 의 최댓값 구하기
answer = 0
for i in range(1, n + 1):
    if dist_from_x[i] != float('inf') and dist_to_x[i] != float('inf'):
        total_cost = dist_from_x[i] + dist_to_x[i]
        answer = max(answer, total_cost)

print(answer)