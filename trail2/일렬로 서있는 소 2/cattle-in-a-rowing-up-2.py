n = int(input())
a = list(map(int, input().split()))

answer = 0

# n이 100 이상일 때 - 가운데를 기준으로 잡기 - 2중 for문 - O(N^2)
for j in range(1, n - 1):
    left_count = 0
    right_count = 0

    for i in range(j):
        if a[i] <= a[j]:
            left_count += 1
    
    for k in range(j + 1, n):
        if a[k] >= a[j]:
            right_count += 1

    answer += (left_count * right_count)

print(answer)


# n이 100이하일때 - 3중 for문 - O(N^3)
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if i < j < k and a[i] <= a[j] <= a[k]:
#                 answer += 1

# print(answer)