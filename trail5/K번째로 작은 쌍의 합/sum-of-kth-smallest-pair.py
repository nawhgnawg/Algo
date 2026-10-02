import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 1. 두 배열 오름차순 정렬
arr1.sort()
arr2.sort()

pq = []

# 2. arr1의 원소들과 arr2[0]의 합을 힙에 초기화 (최대 k개만 넣어도 충분)
for i in range(min(n, k)):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

answer = 0

# 3. k번 pop을 수행하며 k번째로 작은 합을 추출
for _ in range(k):
    sum_val, i, j = heapq.heappop(pq)
    answer = sum_val

    # 꺼낸 조합의 다음 arr2 원소(j + 1)가 존재하면 힙에 추가
    if j + 1 < m:
        heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))

print(answer)
