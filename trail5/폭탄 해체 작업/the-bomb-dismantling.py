import heapq

N = int(input())
bombs = []
max_time = 0

for _ in range(N):
    point, time = map(int, input().split())
    bombs.append((point, time))
    if time > max_time:
        max_time = time

# 폭탄들을 시간 제한 기준 '내림차순(큰 순서대로)' 정렬합니다.
bombs.sort(key=lambda x: x[1], reverse=True)

total_point = 0
bomb_idx = 0
heap = [] # 현재 시간대에서 고를 수 있는 폭탄들의 점수를 담는 최대 힙

# 가장 넉넉한 마감 시간부터 1초까지 거꾸로(역순) 흘러갑니다.
for t in range(max_time, 0, -1):
    
    # 현재 시간 t보다 시간 제한이 크거나 같은 폭탄들을 전부 힙에 집어넣습니다.
    # (t초에 해체해도 안전한 폭탄들을 모으는 과정입니다.)
    while bomb_idx < N and bombs[bomb_idx][1] >= t:
        # 파이썬 heapq는 최소 힙이므로 최대 힙 효과를 내기 위해 점수에 -를 붙여 넣습니다.
        heapq.heappush(heap, -bombs[bomb_idx][0])
        bomb_idx += 1
        
    # 이번 t초에 해체할 수 있는 후보 폭탄이 바구니(힙)에 존재한다면
    if heap:
        # 그중 가장 점수가 높은 녀석(최솟값의 마이너스)을 꺼내어 더해줍니다.
        total_point += (-heapq.heappop(heap))

print(total_point)
