N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_num = -1

# for i in range(N - 1):
#     for j in range(i, i + K + 1):

#         # 자기 자신은 스킵
#         if i == j:
#             continue

#         # 인덱스 + 조건 체크 후 최댓값 갱신
#         if j < N and num[i] == num[j]:
#             max_num = max(max_num, num[j])

for i in range(N - 1):
    if num[i] in num[i + 1: i + K + 1]:
        max_num = max(max_num, num[i])
        
print(max_num)
        