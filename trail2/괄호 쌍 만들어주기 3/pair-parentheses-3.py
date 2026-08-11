a = input()

n = len(a)

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        curr_a = a[i]
        if curr_a == '(' and a[j] == ')':
            answer += 1

print(answer)
            
        
