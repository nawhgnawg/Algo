n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_dist = float('inf')

# 건너 뛸 수 있는 체크포인트(i) 
for i in range(1, n - 1):
    curr_x, curr_y = points[0]
    curr_dist = 0
    # 거리 계산
    for j in range(1, n):
        if i == j:
            continue
        x, y = points[j]
        dist = abs(x - curr_x) + abs(y - curr_y)
        curr_dist += dist
        curr_x, curr_y = x, y
    
    min_dist = min(curr_dist, min_dist)

print(min_dist)
