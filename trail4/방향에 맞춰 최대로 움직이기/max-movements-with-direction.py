n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 방향에 따른 이동
di = {1: (-1, 0), 2: (-1, 1), 3: (0, 1), 4: (1, 1), 5: (1, 0), 6: (1, -1), 7: (0, -1), 8: (-1, -1)}

# 시작점 index0에 맞추기
r -= 1
c -= 1

max_count = 0

def dfs(cr, cc, count):
    global max_count
    
    # 매 이동마다 최대 이동 횟수를 갱신
    max_count = max(max_count, count)

    # 현재 칸의 방향 가져오기
    dx, dy = di[move_dir[cr][cc]]

    # 해당 방향으로 1칸부터 n-1칸까지 멀어지며 탐색
    for i in range(1, n):
        nx = cr + (dx * i)
        ny = cc + (dy * i)

        if 0 <= nx < n and 0 <= ny < n and num[cr][cc] < num[nx][ny]:
            # 다음 칸으로 이동하며 이동 횟수(count)를 1 증가시킴
            dfs(nx, ny, count + 1)

# 시작 위치에서 이동 횟수 0으로 DFS 시작
dfs(r, c, 0)

print(max_count)
    
