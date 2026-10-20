import heapq

n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(sx, sy):
    dist = [[float('inf')] * n for _ in range(n)]
    pq = []

    dist[sx][sy] = 0
    heapq.heappush(pq, (0, sx, sy))

    max_d = 0

    while pq:
        d, x, y = heapq.heappop(pq)

        if dist[x][y] < d:
            continue
        
        max_d = max(max_d, d)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = a if grid[x][y] == grid[nx][ny] else b

                if d + cost < dist[nx][ny]:
                    dist[nx][ny] = d + cost
                    heapq.heappush(pq, (d + cost, nx, ny))

    return max_d

ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, dijkstra(x, y))

print(ans)



