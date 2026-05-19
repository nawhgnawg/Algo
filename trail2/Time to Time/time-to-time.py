a, b, c, d = map(int, input().split())

before = a * 60 + b
after = c * 60 + d

print(after - before)