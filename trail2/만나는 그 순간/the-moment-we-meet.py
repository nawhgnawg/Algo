n, m = map(int, input().split())

MAX_T = 1000000
pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

# 1. A의 1초 단위 이동 기록
time_a = 1
for _ in range(n):
    d, dist = input().split()
    dist = int(dist)
    
    for _ in range(dist):
        if d == 'R':
            pos_a[time_a] = pos_a[time_a - 1] + 1
        elif d == 'L':
            pos_a[time_a] = pos_a[time_a - 1] - 1
        time_a += 1

# 2. B의 1초 단위 이동 기록
time_b = 1
for _ in range(m):
    d, dist = input().split()
    dist = int(dist)

    for _ in range(dist):
        if d == 'R':
            pos_b[time_b] = pos_b[time_b - 1] + 1
        elif d == 'L':
            pos_b[time_b] = pos_b[time_b - 1] - 1
        time_b += 1

answer = -1
for t in range(1, time_a):
    if pos_a[t] == pos_b[t]:
        answer = t
        break

print(answer)