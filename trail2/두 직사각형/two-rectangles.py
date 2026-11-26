x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# 밑에 있는 경우, 위에 있는 경우, 왼쪽에 있는경우, 아래쪽에 있는경우
if (x1 <= a2 and x2 >= a1) and (y1 <= b2 and y2 >= b1):
    print("overlapping")
else:
    print("nonoverlapping")