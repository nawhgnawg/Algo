n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

sorted_name = sorted(name)

print('name')
for i in range(len(name)):
    idx = name.index(sorted_name[i])
    print(f'{name[idx]} {height[idx]} {weight[idx]}')

sorted_height = sorted(height, reverse=True)

print("")
print("height")
for i in range(len(sorted_height)):
    idx = height.index(sorted_height[i])
    print(f'{name[idx]} {height[idx]} {weight[idx]}')