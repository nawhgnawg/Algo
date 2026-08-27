n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i, n):
        sub = arr[i : j + 1]
        length = len(sub)
        total = sum(sub)
        
        # 합이 구간 길이로 나누어떨어지고, 그 평균값(정수)이 부분 배열에 있는 경우
        if total % length == 0 and (total // length) in sub:
            answer += 1

print(answer)

# answer = n

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         # 구간(i ~ j)까지 
#         avg = sum(arr[i: j + 1]) / (j - i + 1)
#         if avg in arr[i: j + 1]:
#             answer += 1

# print(answer)
