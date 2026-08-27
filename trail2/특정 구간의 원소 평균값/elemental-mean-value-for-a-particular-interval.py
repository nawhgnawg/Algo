n = int(input())
arr = list(map(int, input().split()))

answer = n

for i in range(n - 1):
    for j in range(i + 1, n):
        # 구간(i ~ j)까지 
        avg = sum(arr[i: j + 1]) / (j - i + 1)
        if avg in arr[i: j + 1]:
            answer += 1

print(answer)
