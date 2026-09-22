import heapq
from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))

counts = Counter(arr)

# Python heapq는 기본이 Min-Heap이므로 (빈도, 값)으로 넣어 최소 원소를 pop
heap = []
for num, count in counts.items():
    heapq.heappush(heap, (count, num))
    if len(heap) > k:
        heapq.heappop(heap)

# 남은 K개 추출 후 요구 정렬 조건에 맞게 역순 정렬
result = [num for count, num in sorted(heap, key=lambda x: (x[0], x[1]), reverse=True)]
print(*result)


# # 1. 숫자의 등장 빈도 집계 (O(N))
# counts = Counter(arr)

# # 2. 정렬 조건 적용 (O(U log U), U는 유일한 숫자의 개수)
# # 1순위: counts[x] (빈도수 내림차순)
# # 2순위: x (숫자 크기 내림차순)
# sorted_nums = sorted(counts.keys(), key=lambda x: (counts[x], x), reverse=True)

# # 3. 상위 k개 원소 출력
# print(*(sorted_nums[:k]))

