n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

di = {'U': (-1, 0, 'D'), 'D': (1, 0, 'U'), 'R': (0, 1, 'L'), 'L': (0, -1, 'R')}

current_d = d
current_r = r
current_c = c
 
while t > 0:
    t -= 1

    dr, dc, next_d = di[current_d]
    
    # 이동
    nr = current_r + dr
    nc = current_c + dc

    # 범위 넘어가면 방향 변경
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        current_d = next_d
    elif 0 <= nr < n and 0 <= nc < n:
        current_r = nr
        current_c = nc

print(current_r + 1, current_c + 1)