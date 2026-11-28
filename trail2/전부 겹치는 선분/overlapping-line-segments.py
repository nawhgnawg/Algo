n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

min_x = min(x1 for x1, _ in segments)
max_x = max(x2 for _, x2 in segments)

answer = "No"
# 확인 할 범위 
for i in range(min_x, max_x + 1):
    checked = [False] * n
    for idx, (x1, x2) in enumerate(segments):
        if x1 <= i <= x2:
            checked[idx] = True
    
    count = 0
    for c in checked:
        if c == True:
            count += 1
    
    if count == n:
        answer = "Yes"
        break

print(answer)