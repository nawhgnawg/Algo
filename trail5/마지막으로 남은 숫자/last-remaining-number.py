import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []
for num in arr:
    heapq.heappush(pq, -num)

while len(pq) >= 2:
    num1 = -heapq.heappop(pq)
    num2 = -heapq.heappop(pq)

    dist = num1 - num2
    if dist != 0:
        heapq.heappush(pq, -dist)

if pq:
    print(-pq[0])
else:
    print(-1)