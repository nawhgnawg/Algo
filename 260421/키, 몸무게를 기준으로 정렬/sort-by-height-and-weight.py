n = int(input())

info = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    info.append((n_i, int(h_i), int(w_i)))

info.sort(key=lambda x: (x[1], -x[2]))

for n, h, w in info:
    print(f'{n} {h} {w}')