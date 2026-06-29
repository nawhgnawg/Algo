n = int(input())
moves = [tuple(input().split()) for _ in range(n)]

# N, S, W, E
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
di = {'W': (-1, 0), 'S': (0, -1), 'N': (0, 1), 'E': (1, 0)}

x, y = 0, 0

for move in moves:
    dir, dist = move[0], int(move[1])

    dx, dy = di[dir]

    for i in range(dist):
        x += dx
        y += dy

print(x, y)

