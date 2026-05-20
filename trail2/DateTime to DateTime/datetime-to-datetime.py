a, b, c = map(int, input().split())

before_m = 11 * 24 * 60 + 11 * 60 + 11
after_m = a * 24 * 60 + b * 60 + c

ans = after_m - before_m

if ans < 0:
    print(-1)
else:
    print(ans)