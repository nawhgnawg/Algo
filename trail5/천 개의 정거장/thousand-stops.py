import heapq

A, B, N = map(int, input().split())

# graph[u][v] = (min_cost, min_time) 최적 간선만 저장
graph = [{} for _ in range(1001)]

for _ in range(N):
    cost, stop_count = map(int, input().split())
    stops = list(map(int, input().split()))

    # 해당 버스 노선 내의 모든 (u -> v) 경로 추가 (u가 v보다 먼저 나오는 경우만)
    for i in range(stop_count):
        for j in range(i + 1, stop_count):
            u, v = stops[i], stops[j]
            time = j - i  # 소요 시간 = 정거장 간격 수

            # 이미 u -> v 간선이 있다면 더 이득인 조건(비용, 시간)으로만 갱신
            if v not in graph[u] or (cost, time) < graph[u][v]:
                graph[u][v] = (cost, time)
    
# dist[i] = (최소 비용, 최소 버스 수)
dist = [(float('inf'), float('inf'))] * 1001

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, 0, start))
    dist[start] = (0, 0)

    while pq:
        cur_cost, cur_time, cur = heapq.heappop(pq)

        # 현재 꺼낸 정보가 이미 기록된 최단 거리보다 좋지 않다면 스킵
        if dist[cur] < (cur_cost, cur_time):
            continue
        
        for next_node, (cost, time) in graph[cur].items():
            next_cost = cur_cost + cost
            next_time = cur_time + time  # 정거장 간격(소요 시간) 누적

            # (비용 우선, 같은 비용이면 소요 시간 최소) 사전순 비교
            if (next_cost, next_time) < dist[next_node]:
                dist[next_node] = (next_cost, next_time)
                heapq.heappush(pq, (next_cost, next_time, next_node))

dijkstra(A)

ans_cost, ans_buses = dist[B]

if ans_cost == float('inf'):
    print("-1 -1")
else:
    print(ans_cost, ans_buses)