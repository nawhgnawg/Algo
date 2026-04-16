n = int(input())
info = []

for _ in range(n):
    name, korean, english, math = input().split()
    info.append((name, int(korean), iint(english), int(math)))

info.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for name, korean, english, math in info:
    print(f'{name} {korean} {english} {math}')
