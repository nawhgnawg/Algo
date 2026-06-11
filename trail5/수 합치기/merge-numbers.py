import heapq

n = int(input())
arr = list(map(int, input().split()))


# 1. 기존 리스트를 최소 힙(Min Heap) 구조로 변환 (O(N))
heapq.heapify(arr)

total_cost = 0

# 2. 힙에 숫자가 딱 1개 남을 때까지 반복합니다.
while len(arr) > 1:
    # 가장 작은 숫자 2개를 꺼냅니다 (각각 O(log N))
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    
    # 두 숫자를 합치는 비용 계산
    cost = first + second
    total_cost += cost
    
    # 합쳐진 새로운 숫자를 다시 힙에 넣습니다 (O(log N))
    heapq.heappush(arr, cost)

print(total_cost)