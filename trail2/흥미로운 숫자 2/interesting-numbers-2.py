x, y = map(int, input().split())

answer = 0

for num in range(x, y + 1):
    str_num = str(num)
    dic = {}
    for i in range(len(str_num)):
        if not str_num[i] in dic:
            dic[str_num[i]] = 1
        else:
            dic[str_num[i]] += 1
    
    if len(dic.keys()) == 2:
        for v in dic.values():
            if v == 1:
                answer += 1
        
print(answer)
        
