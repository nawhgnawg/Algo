n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

answer = []
for i in range(n):
    remaining = [times[j] for j in range(n) if j != i]

    t = [0] * 1002

    for start, end in remaining:
        for k in range(start, end):
            if t[k] == 0:
                t[k] += 1
    answer.append(t.count(1))

print(max(answer))
