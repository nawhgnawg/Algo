dirs = input()

# N, W, S, E
di = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

x, y = 0, 0
dir = 0

for i in range(len(dirs)):
    if dirs[i] == 'F':
        dx, dy = di[dir]
        x += dx
        y += dy
    elif dirs[i] == 'L':
        dir = (dir + 1) % 4
    elif dirs[i] == 'R':
        dir = (dir + 3) % 4

print(x, y)


