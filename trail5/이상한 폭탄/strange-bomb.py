n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_num = -1
latest_idx = {}

for i in range(n):
    num = arr[i]

    # 1. 현재 폭탄 번호가 이전에 등장한 적이있고,
    # 2. 현재 인덱스(i)와 가장 최근 등장한 인덱스의 차이가 k 이하라면 폭발 
    if num in latest_idx and i - latest_idx[num] <= k:
        max_num = max(max_num, num)

    latest_idx[num] = i

# for i in range(n - 1):
#     if arr[i] in arr[i + 1: i + k + 1]:
#         max_num = max(max_num, arr[i])

# for i in range(n):
#     for j in range(i + 1, i + k + 1):

#         if j < n:
#             # 같은 번호가 있으면
#             if arr[i] == arr[j]:
#                 max_num = max(max_num, arr[i])

print(max_num)