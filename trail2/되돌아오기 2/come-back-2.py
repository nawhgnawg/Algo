commands = input()

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

x, y = 0, 0
OFFSET = 0
curr_dx, curr_dy = dx[OFFSET], dy[OFFSET]
count = 0

for d in commands:
    if d == 'F':
        x += curr_dx
        y += curr_dy
    elif d == 'R':
        OFFSET = (OFFSET + 3) % 4
        curr_dx, curr_dy = dx[OFFSET], dy[OFFSET]
    elif d == 'L':
        OFFSET = (OFFSET + 1) % 4
        curr_dx, curr_dy = dx[OFFSET], dy[OFFSET]

    count += 1

    if x == 0 and y == 0:
        print(count)
        exit()

print(-1)