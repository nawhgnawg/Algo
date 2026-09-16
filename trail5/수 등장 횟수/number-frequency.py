n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

dic = {}

for num in arr:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

for num in nums:
    if num in dic:
        print(dic[num], end=" ")
    else:
        print(0, end=" ")