import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for idx in range(m):
    u, v, aw, bw = map(int, input().split())
    # 그림 A와 그림 B의 가중치를 하나의 간선 정보로 묶어서 관리 (다중 간선 대응)
    graph[u].append((v, aw, bw, idx))
    rev_graph[v].append((u, aw, bw, idx))

# 1. 목적지 N에서 출발하는 역방향 다익스트라 (각 정점에서 N까지의 최단 거리 계산)
def dijkstra_reverse(rev_graph_target, weight_idx):
    dist = [float('inf')] * (n + 1)
    pq = []
    
    heapq.heappush(pq, (0, n))
    dist[n] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, aw, bw, idx in rev_graph_target[cur]:
            # weight_idx가 0이면 그림 A(aw), 1이면 그림 B(bw) 선택
            w = aw if weight_idx == 0 else bw
            cost = d + w
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
                
    return dist

# 그림 A와 그림 B 각각에서 모든 정점 -> N까지의 최단 거리 구하기
dist_to_n_a = dijkstra_reverse(rev_graph, 0)
dist_to_n_b = dijkstra_reverse(rev_graph, 1)

# 2. 1번에서 N번까지 이동할 때 최소 경고 횟수를 구하는 다익스트라
def find_min_warnings():
    min_warnings = [float('inf')] * (n + 1)
    pq = []
    
    # (누적 경고 횟수, 현재 정점)
    heapq.heappush(pq, (0, 1))
    min_warnings[1] = 0

    while pq:
        warnings, cur = heapq.heappop(pq)

        if warnings > min_warnings[cur]:
            continue

        if cur == n:
            return warnings

        for next_node, aw, bw, idx in graph[cur]:
            add_warning = 0
            
            # 현재 정점(cur)을 기점으로 N까지 가는 최단 거리 조건에 부합하는지 확인
            # 조건: dist[cur] == weight + dist[next_node]
            if dist_to_n_a[cur] != aw + dist_to_n_a[next_node]:
                add_warning += 1
            
            if dist_to_n_b[cur] != bw + dist_to_n_b[next_node]:
                add_warning += 1

            next_warnings = warnings + add_warning

            if next_warnings < min_warnings[next_node]:
                min_warnings[next_node] = next_warnings
                heapq.heappush(pq, (next_warnings, next_node))

    return -1

print(find_min_warnings())