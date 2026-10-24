import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for edge_idx in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d, edge_idx))
    graph[j].append((i, d, edge_idx))

def dijkstra(target_edge_idx):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)  # 경로 역추적을 위한 부모 노드 기록
    pq = []
    heapq.heappush(pq, (0, 1))
    dist[1] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, weight, edge_idx in graph[cur]:
            # 만약 현재 간선이 2배로 늘려야 하는 대상이라면 가중치를 2배로 적용
            if edge_idx == target_edge_idx:
                actual_weight = weight * 2
            else:
                actual_weight = weight

            cost = d + actual_weight

            if cost < dist[next_node]:
                dist[next_node] = cost
                parent[next_node] = cur  # 어디서 왔는지 기록
                heapq.heappush(pq, (cost, next_node))
    
    return dist, parent

# 1. 기본 상태에서 최단 거리와 경로 구하기
original_dist, parent = dijkstra(-1)
original_shortest = original_dist[n]

# 2. 1번 노드에서 N번 노드로 가는 최단 경로에 포함된 간선(edge_idx)들 수집
path_edges = set()
curr = n
while curr != 1:
  p = parent[curr]
  # p에서 curr로 연결된 간선의 인덱스 찾기
  for next_node, weight, edge_idx in graph[p]:
    if next_node == curr:
      path_edges.add(edge_idx)
      break
  curr = p

# 3. 최단 경로 상의 간선들을 하나씩만 2배로 늘려보며 최단 거리의 최댓값 갱신
max_shortest_path = 0

for edge_idx in path_edges:
  dist, _ = dijkstra(edge_idx)
  max_shortest_path = max(max_shortest_path, dist[n])

# 4. (늘렸을 때의 최대 최단 거리) - (원래의 최단 거리) 출력
print(max_shortest_path - original_shortest)