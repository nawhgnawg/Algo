import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
c_values = set()

for _ in range(m):
    i, j, l, c = map(int, input().split())
    graph[i].append((j, l, c))
    graph[j].append((i, l, c))
    c_values.add(c)  # 존재할 수 있는 A 후보 수집


def dijkstra(min_c):
    dist = [float('inf')] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, 1))
    dist[1] = 0

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] < d:
            continue
        
        for next_node, l, c in graph[cur]:
            # C값이 min_c 이상인 간선만 이용 가능
            if c >= min_c:
                cost = d + l
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(pq, (cost, next_node))

    return dist[n]  # 1번에서 N번까지의 최소 L의 합 B

ans = float('inf')

for target_c in c_values:
    b = dijkstra(target_c)
    
    if b != float('inf'):
        # 실수 나눗셈 후 전체 값의 소수점 버림 처리
        total_time = int(b + (x / target_c))
        ans = min(ans, total_time)

print(ans)