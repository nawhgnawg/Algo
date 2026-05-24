n = int(input())

commands = [tuple(map(str, input().split())) for _ in range(n)]

count = [0] * 2001

current_x = 1000
for dist, d in commands:
    
    if d == 'R':
        for i in range(current_x, current_x + int(dist)):
            count[i] += 1
        
        current_x = current_x + int(dist)

    elif d == 'L':
        for i in range(current_x - int(dist), current_x):
            count[i] += 1
        
        current_x = current_x - int(dist)
    
answer = 0
for n in count:
    if n >= 2:
        answer += 1

print(answer)
            