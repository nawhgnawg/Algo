n = int(input())
h = [int(input()) for _ in range(n)]

max_area = 0

for s in range(max(h)):
    area = 0
    is_new = False
    new_h = [c - s for c in h]
    for curr_h in new_h:
        if curr_h > 0:
            # 새로운 덩어리라면
            if is_new == False:
                area += 1
                is_new = True
        else:
            is_new = False
    
    max_area = max(area, max_area)

print(max_area)