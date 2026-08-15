a = list(input())

changed = False

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        changed = True
        break

if not changed:
    a[-1] = '0'

answer_str = "".join(a)
print(int(answer_str, 2))
    
