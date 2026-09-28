import heapq

n = int(input())

min_heap = []

for _ in range(n):
    x = int(input())
    
    if x > 0:
        heapq.heappush(min_heap, x)
    else:
        # 배열이 비어있는 경우 0 출력
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
