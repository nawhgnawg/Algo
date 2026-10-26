import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 사전순 탐색을 위해 각 정점의 인접 리스트 정렬 (도착 정점 번호 기준)
for i in range(1, n + 1):
    graph[i].sort()

# 1. 목적지 N에서 출발하는 다익스트라 (모든 정점에서 N까지의 최단 거리 계산)
def dijkstra_from_n():
    dist = [float('inf')] * (n + 1)
    pq = []
    
    heapq.heappush(pq, (0, n))
    dist[n] = 0

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

dist_from_n = dijkstra_from_n()

# 2. 1번에서 N번으로 가는 '사전순 최단 경로' 그리디하게 찾기
curr = 1
a_edges = set()

while curr != n:
    for next_node, weight in graph[curr]:
        # 최단 경로 상에 놓이는 조건: 현재 정점까지의 거리 == 간선 가중치 + 다음 정점에서 N까지의 최단 거리
        if dist_from_n[curr] == weight + dist_from_n[next_node]:
            # 인접 리스트가 이미 정렬되어 있으므로 처음 만나는 후보가 '사전순으로 가장 앞서는' 정점임
            a_edges.add((min(curr, next_node), max(curr, next_node)))
            curr = next_node
            break

# 3. B의 다익스트라 (1번에서 출발, A가 사용한 간선들은 제외)
def dijkstra_B():
    dist = [float('inf')] * (n + 1)
    pq = []

    heapq.heappush(pq, (0, 1))
    dist[1] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, weight in graph[cur]:
            # A가 사용한 간선이면 건너뛰기
            if (min(cur, next_node), max(cur, next_node)) in a_edges:
                continue

            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
                
    return dist

b_dist = dijkstra_B()

# 4. 결과 출력 (도달할 수 없다면 -1)
print(b_dist[n] if b_dist[n] != float('inf') else -1)