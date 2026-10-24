import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for idx in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w, idx))
    graph[v].append((u, w, idx))

def dijkstra(trim_idx):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    pq = []

    heapq.heappush(pq, (0, 1))
    dist[1] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue

        for next_node, weight, edge_idx in graph[cur]:
            # 제거해야 하는 간선 번호라면 탐색에서 제외 (간선 삭제 효과)
            if edge_idx == trim_idx:
                continue

            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                parent[next_node] = cur
                parent_edge[next_node] = edge_idx
                heapq.heappush(pq, (cost, next_node))
    
    return dist, parent, parent_edge

# 1. 기본 상태에서 최단 거리 구하기
orig_dist, orig_parent, orig_parent_edge = dijkstra(-1)
original_shortest = orig_dist[n]

# 2. 1번 노드에서 N번 노드로 가는 최단 경로에 포함된 간선 인덱스들 수집
path_edges = set()
curr = n
while curr != 1:
    edge_idx = orig_parent_edge[curr]
    if edge_idx != -1:
        path_edges.add(edge_idx)
    curr = orig_parent[curr]

# 3. 최단 경로 상의 간선들을 하나씩만 제거해보며 최단 거리가 증가하는지 확인
answer = 0

for edge_idx in path_edges:
    dist, _, _ = dijkstra(edge_idx)
    # 간선을 지웠을 때 최단 거리가 기존보다 커지거나(다른 우회로가 없거나 더 긺), 도달할 수 없게 되면(inf) 정답 카운트 증가
    if dist[n] > original_shortest:
        answer += 1

print(answer)

