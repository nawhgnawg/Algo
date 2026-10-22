import heapq

n, m = map(int, input().split())
red1, red2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
    graph[j].append((i, d))

def dijkstra(start):
    dist = [float('inf')] * (n + 1)
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

    return dist

# 1. red1과 red2에서 출발하는 다익스트라 각각 실행
dist_red1 = dijkstra(red1)
dist_red2 = dijkstra(red2)

# red1과 red2 사이의 최단 거리
red_to_red = dist_red1[red2]

ans = float('inf')

# 빨간 점을 제외한 모든 검은 점 S를 시작 후보로 확인
for s in range(1, n + 1):
    if s == red1 or s == red2:
        continue
    
    # S -> red1 -> red2 -> S 경로의 총 거리
    # S <-> red1 왕복 (dist_red1[s] * 2) + red1 <-> red2 (red_to_red) + S <-> red2 왕복 (dist_red2[s] * 2)
    if dist_red1[s] != float('inf') and dist_red2[s] != float('inf') and red_to_red != float('inf'):
        total_dist = dist_red1[s] + red_to_red + dist_red2[s]
        ans = min(ans, total_dist)

if ans == float('inf'):
    print(-1)
else:
    print(ans)