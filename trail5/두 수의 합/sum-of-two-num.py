from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
answer = 0

for x in arr:
    target = k - x

    # 1. 이전까지 등장한 (k - x)의 개수만큼 쌍을 만들 수 있음
    if target in count:
        answer += count[target]

    # 2. 현재 숫자 x의 등장 횟수를 기록
    count[x] += 1

print(answer)

# for i in range(n):
#     for j in range(i + 1, n):
#         s = arr[i] + arr[j]
#         if s not in dic:
#             dic[s] = 1
#         else:
#             dic[s] += 1

# if k in dic:
#     print(dic[k])
# else:
#     print(0)