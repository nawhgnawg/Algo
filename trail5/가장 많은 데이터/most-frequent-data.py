n = int(input())
words = [input() for _ in range(n)]

dic = {}

for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print(max(dic.values()))