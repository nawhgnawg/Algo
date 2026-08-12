n = int(input())
a = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if i < j < k and a[i] <= a[j] <= a[k]:
                answer += 1

print(answer)