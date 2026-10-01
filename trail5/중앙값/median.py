import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    max_heap = []
    min_heap = []

    for i, val in enumerate(arr):
        # 1. max_heap에 넣은 뒤, 가장 큰 값을 min_heap으로 보냄
        val = heapq.heappushpop(max_heap, -val)
        heapq.heappush(min_heap, -val)

        # 2. min_heap의 개수가 더 많아지면 max_heap으로 하나 옮겨 균형을 맞춤
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 3. 중앙값 출력 (max_heap의 루트)
        if i % 2 == 0:
            print(-max_heap[0], end=" ")
    print()