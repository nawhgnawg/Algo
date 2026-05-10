n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    remaining = [times[j] for j in range(n) if j != i]

    t = [0] * 1002

    for start, end in remaining:
        for k in range(start, end):
            t[k] = 1

    answer = max(answer, sum(t))

print(answer)
