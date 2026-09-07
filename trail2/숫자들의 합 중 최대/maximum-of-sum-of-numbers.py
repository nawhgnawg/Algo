x, y = map(int, input().split())

max_sum = 0

for i in range(x, y + 1):
    sum = 0
    curr_num = i
    while curr_num > 0:
        sum += curr_num % 10 
        curr_num //= 10
    max_sum = max(max_sum, sum)

print(max_sum)

