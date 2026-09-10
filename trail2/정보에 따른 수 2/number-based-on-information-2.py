t, a, b = map(int, input().split())

s_pos = []
n_pos = []

# 1. S와 N의 위치를 각각 리스트에 저장합니다.
for _ in range(t):
    char, pos = input().split()
    if char == 'S':
        s_pos.append(int(pos))
    else:
        n_pos.append(int(pos))

answer = 0

# 2. a부터 b까지 모든 정수 위치 k에 대해 최단 거리를 측정합니다.
for k in range(a, b + 1):
    # k에서 가장 가까운 S와의 거리
    d1 = min(abs(k - s) for s in s_pos)
    # k에서 가장 가까운 N과의 거리
    d2 = min(abs(k - n) for n in n_pos)

    # S와의 최단 거리가 N과의 최단 거리 이하인 경우
    if d1 <= d2:
        answer += 1

print(answer)