n, m = map(int, input().split())


pos_a = [0]
pos_b = [0]

time_a = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)

    if d == 'L':
        for _ in range(t):
            pos_a.append(pos_a[-1] - 1)
            time_a += 1
    elif d == 'R':
        for _ in range(t):
            pos_a.append(pos_a[-1] + 1)
            time_a += 1
    
time_b = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)

    if d == 'L':
        for _ in range(t):
            pos_b.append(pos_b[-1] - 1)
            time_b += 1
    elif d == 'R':
        for _ in range(t):
            pos_b.append(pos_b[-1] + 1)
            time_b += 1


answer = 0
max_time = max(len(pos_a), len(pos_b))

# A가 먼저 끝났다면 마지막 위치를 복사해서 늘려줌
while len(pos_a) < max_time:
    pos_a.append(pos_a[-1])

# B가 먼저 끝났다면 마지막 위치를 복사해서 늘려줌
while len(pos_b) < max_time:
    pos_b.append(pos_b[-1])

for i in range(1, max_time):
    # 지금은 같은 위치인데, 1초 전에는 다른 위치였다면? = 새롭게 만난 것!
    if pos_a[i] == pos_b[i] and pos_a[i-1] != pos_b[i-1]:
        answer += 1
        
print(answer)