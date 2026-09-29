import heapq

n, m = map(int, input().split())

# (x + y, x, y) 형태의 튜플로 힙 생성
pq = []

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, (x + y, x, y))

# m번 동안 가장 가까운 점을 뽑아 (x+2, y+2) 갱신 후 다시 push
for _ in range(m):
    dist, x, y = heapq.heappop(pq)
    
    nx, ny = x + 2, y + 2
    heapq.heappush(pq, (nx + ny, nx, ny))

# 가장 가까운 점의 x, y 좌표 출력
_, ans_x, ans_y = pq[0]
print(ans_x, ans_y)