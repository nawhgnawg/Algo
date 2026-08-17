a = list(input().strip())

left = 0

answer = 0

for i in range(len(a) - 1):
    if a[i] == '(' and a[i + 1] == '(':
        left += 1
    
    if a[i] == ')' and a[i + 1] == ')':
        answer += left

print(answer)