n, k = map(int, input().split())

MAX_X = 10000

# 1. 1차원 좌표 배열 초기화 (좌표 1 ~ 10000)
points = [0] * (MAX_X + 1)

for _ in range(n):
    pos, char = input().split()
    points[int(pos)] = 1 if char == 'G' else 2

# 2. k가 최대 좌표 범위를 넘어서는 경우, 모든 점수의 합이 정답
if k >= MAX_X:
    print(sum(points))
else:
    max_score = 0
    
    # 3. 좌표 i부터 i+k까지의 합(길이 k인 구간)을 순차적으로 탐색
    for i in range(1, MAX_X - k + 1):
        curr_score = sum(points[i : i + k + 1])
        max_score = max(max_score, curr_score)
        
    print(max_score)