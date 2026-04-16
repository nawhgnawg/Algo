n = int(input())
name = []
height = []
weight = []

info = []


for _ in range(n):
    n_i, h_i, w_i = input().split()
    info.append((n_i, int(h_i), int(w_i)))

info.sort(key=lambda x: x[1])
for i in range(len(info)):
    print(f'{info[i][0]} {info[i][1]} {info[i][2]}')