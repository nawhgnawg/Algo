n, m, k = map(int, input().split())
students = [int(input()) for _ in range(m)]

arr = [0] * (n + 1)

answer = -1

for st in students:
    arr[st] += 1
    if arr[st] >= k:
        answer = st
        break

print(answer)





