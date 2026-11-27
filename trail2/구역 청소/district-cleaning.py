a, b = map(int, input().split())
c, d = map(int, input().split())

answer = 0

# 겹칠 때
if a <= d and b >= c:
    start = min(a, c)
    end = max(b, d)
    answer = end - start
else:
    answer = (b - a) + (d - c)

print(answer)