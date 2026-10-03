import heapq

n = int(input())

pq = []
for _ in range(n):
    num = int(input())
    if num != 0:
        # (절댓값, 실제값) 튜플로 힙에 push
        heapq.heappush(pq, (abs(num), num))
    else:
        if not pq:
            print(0)
        else:
            # 가장 우선순위가 높은 (절댓값, 실제값)을 꺼내서 실제값만 출력
            abs_val, val = heapq.heappop(pq)
            print(val)