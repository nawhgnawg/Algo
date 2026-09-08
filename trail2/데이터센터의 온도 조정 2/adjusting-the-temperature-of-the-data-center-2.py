n, c, g, h = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

min_t = min(a for a, _ in ranges)
max_t = max(b for _, b in ranges)

max_sum = 0

# 0도 ~ 최대 도까지
for temp in range(min_t - 1, max_t + 2):
    curr_sum = 0
    for a, b in ranges:
        if temp < a:
            curr_sum += c
        elif temp <= b:
            curr_sum += g
        elif temp > b:
            curr_sum += h
        
    max_sum = max(curr_sum, max_sum)

print(max_sum)
     

