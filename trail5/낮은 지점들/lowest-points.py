n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# x값들이 처음이면 y 그대로 넣고, 이미 있는 x값이라면 최소값 비교
dic = {}

for x, y in points:
    if x not in dic:
        dic[x] = y
    else:
        dic[x] = min(dic[x], y)

print(sum(dic.values()))