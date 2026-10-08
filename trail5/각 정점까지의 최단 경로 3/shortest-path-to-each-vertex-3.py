import heapq

n, m = map(int, input().split())

# 그래프 인접 리스트 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w인 간선

dist = [float('inf')] * (n + 1)

def dijkstra(start):
    pq = []
    # (거리, 노드) 튜플 저장
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        # 이미 최단 거리가 확정된 노드라면 스킵
        if dist[cur] < d:
            continue
        
        # 인접한 노드 탐색
        for next_node, weight in graph[cur]:
            cost = d + weight
            # 더 짧은 경로를 찾은 경우 갱신 후 힙에 삽입
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

# 1번 정점에서 출발
dijkstra(1)

# 각 정점까지의 최단 거리 출력 (도달할 수 없는 경우 -1)
for i in range(2, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])

