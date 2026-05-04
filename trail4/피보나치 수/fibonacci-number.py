N = int(input())

a = [1] * 46

for i in range(1, N):
    a[i + 1] = a[i - 1] + a[i]

print(a[N - 1])