n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

dic = {}
for a, b in pairs:

    if a >= b:
        if (b, a)  not in dic:
            dic[(b, a)] = 1
        else:
            dic[(b, a)] += 1
    else:
        if (a, b) not in dic:
            dic[(a, b)] = 1
        else:
            dic[(a, b)] += 1

print(max(dic.values()))