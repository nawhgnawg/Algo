n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for s, e in meetings:
    if s >= last_end_time:
        count += 1
        last_end_time = e

print(count)

