n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

dic = {}

for num in arr:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for q in queries:
    if q in dic:
        print(dic[q])
    else:
        print(0)