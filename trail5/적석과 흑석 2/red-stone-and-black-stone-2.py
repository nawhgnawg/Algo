import heapq

C, N = map(int, input().split())
T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 정렬
T.sort()
AB.sort(key=lambda x: x[0])  # A 기준 오름차순 정렬

max_pair = 0
pq = []  # B_j를 담을 최소 힙
b_idx = 0  # AB 배열의 인덱스

# 2. 빨간 돌을 작은 것부터 순회
for t in T:
    # 현재 빨간 돌 t 이하의 A를 가지는 검은 돌들의 B를 힙에 삽입
    while b_idx < N and AB[b_idx][0] <= t:
        heapq.heappush(pq, AB[b_idx][1])
        b_idx += 1

    # 현재 빨간 돌 t보다 B가 작은(사용 불가능한) 검은 돌 제거
    while pq and pq[0] < t:
        heapq.heappop(pq)

    # 매칭 가능한 검은 돌 중 B가 가장 작은 것 선택
    if pq:
        heapq.heappop(pq)
        max_pair += 1

print(max_pair)