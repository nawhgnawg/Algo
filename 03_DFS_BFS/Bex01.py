# 1926번 - 그림
# https://www.acmicpc.net/problem/1926

n, m = map(int, input().split())    # n : 세로, m : 가로

data = []
for _ in range(n):
    info = list(map(int, input().split()))
    data.append(info)

# DFS
def dfs(x, y):
    data[x][y] = 0  # 0 이면 체크 안하기 때문에 Visited = True 랑 같은 효과
    # 1. 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    total = 1
    # 2. stack에 좌표 넣기
    stack = list()
    stack.append([x, y])
    # 3. while 문
    while stack:
        # 제일 마지막에 들어온 값 꺼내기
        x, y = stack.pop()
        for i in range(4):  # 상, 하, 좌, 우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:   # 범위 안나가고 값이 1이라면
                stack.append([nx, ny])  # stack에 추가하고
                data[nx][ny] = 0        # data 값을 0으로 만들어 방문 처리
                total += 1              # total에 + 1

    return total


cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            cnt += 1
            ans = max(dfs(i, j), ans)

print(cnt)
print(ans)




