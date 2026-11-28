n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

answer = False
for i in range(n):
    max_x1 = max(x1 for idx, (x1, _) in enumerate(segments) if idx != i)
    min_x2 = min(x2 for idx, (_, x2) in enumerate(segments) if idx != i)

    if max_x1 <= min_x2:
        answer = True
        break

print("Yes" if answer else "No")
    