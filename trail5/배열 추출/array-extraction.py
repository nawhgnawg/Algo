import heapq

n = int(input())

pq = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(pq, -x)
    else:
        if len(pq) == 0:
            print(0)
        else:
            print(-heapq.heappop(pq))

    
