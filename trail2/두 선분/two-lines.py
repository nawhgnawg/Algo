x1, x2, x3, x4 = map(int, input().split())

if x1 <= x4 and x3 <= x2:
    print("intersecting")
else:
    print("nonintersecting")