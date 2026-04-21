n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

dis = []

for i, point in points:
    x, y = point
    current_dis = abs(x) + abs(y)
    dis.append((i + 1, current_dis))

dis.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(dis[i][0])
