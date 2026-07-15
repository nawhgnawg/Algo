n, m = map(int, input().split())

pos_a = [0]
pos_b = [0]

for _ in range(n):
    v, t = map(int, input().split())
    
    for _ in range(t):
        pos_a.append(pos_a[-1] + v)

for _ in range(m):
    v, t = map(int, input().split())
    
    for _ in range(t):
        pos_b.append(pos_b[-1] + v)

answer = 0
# 시작: 0, A선두: 1, B선두: 2, A,B선두: 3
legend = 0

for i in range(1, len(pos_a)):
    if pos_a[i] > pos_b[i]:
        if legend != 1:
            answer += 1
            legend = 1
    elif pos_a[i] < pos_b[i]:
        if legend != 2:
            answer += 1
            legend = 2
    else:
        if legend != 3:
            answer += 1
            legend = 3

print(answer)