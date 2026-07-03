N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

di = {'W': (-1, 0), 'S': (0, -1), 'N': (0, 1), 'E': (1, 0)}

r, c = 0, 0
count = 0

for move in moves:
    dir, dist = move[0], int(move[1])

    dr, dc = di[dir]

    for i in range(dist):
        r += dr
        c += dc
        count += 1
        if r == 0 and c == 0:
            print(count)
            exit()

print(-1)



