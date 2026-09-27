import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 모든 원소를 음수로 바꾸어 Min-Heap에 넣음 (Max-Heap 효과)
pq = [-x for x in arr]
heapq.heapify(pq)


for _ in range(m):
    max_num = -heapq.heappop(pq)
    max_num -= 1
    heapq.heappush(pq, -max_num)

print(-pq[0])