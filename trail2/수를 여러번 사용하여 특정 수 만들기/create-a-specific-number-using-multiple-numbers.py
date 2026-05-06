A, B, C = map(int, input().split())

max_num = 0

for i in range(C // A + 1):
    remaining = C - (A * i)

    j = remaining // B
    
    curr_num = (A * i) + (B * j)

    if curr_num <= C:
        max_num = max(max_num, curr_num)

print(max_num)