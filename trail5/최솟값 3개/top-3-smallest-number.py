import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []

for num in arr:
    heapq.heappush(pq, num)

    if len(pq) < 3:
        print(-1)
        continue
    else:
        # 가장 작은 3개 원소 추출
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        third = heapq.heappop(pq)

        print(first * second * third)

        # 다시 힙에 복구
        heapq.heappush(pq, first)
        heapq.heappush(pq, second)
        heapq.heappush(pq, third)

        # heapq.nsmallest(3, pq)는 편리하지만,
        # 내부적으로 현재 pq에 들어있는 모든 원소를 탐색하면서 가장 작은 3개를 찾아냅니다.O(N^2)
        # nums = heapq.nsmallest(3, pq)
        # result = nums[0] * nums[1] * nums[2]
        # print(result)
