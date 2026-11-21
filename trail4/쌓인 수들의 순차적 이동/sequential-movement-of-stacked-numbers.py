n, m = map(int, input().split())
# 각 칸을 [정수] 형태의 리스트로 초기화
grid = [[[int(x)] for x in input().split()] for _ in range(n)]

move_nums = list(map(int, input().split()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 1부터 N*N까지 각 숫자가 현재 위치한 (r, c) 좌표 저장
nums_idx = [(-1, -1)] * (n * n + 1)
for r in range(n):
    for c in range(n):
        val = grid[r][c][0]
        nums_idx[val] = (r, c)

for num in move_nums:
    curr_r, curr_c = nums_idx[num]
    
    max_val = -1
    max_r, max_c = -1, -1

    for i in range(8):
        nr, nc = curr_r + dx[i], curr_c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
            candidate = max(grid[nr][nc])
            if candidate > max_val:
                max_val = candidate
                max_r, max_c = nr, nc
            
    # 인접한 칸에 숫자가 있는 경우에만 이동
    if max_r != -1:
        curr_stack = grid[curr_r][curr_c]
        idx = curr_stack.index(num)

        # num과 그 위에 쌓인 원소들만 분리
        moving_stack = curr_stack[idx:]
        grid[curr_r][curr_c] = curr_stack[:idx]

        # 목표 칸 맨 위에 쌓기
        grid[max_r][max_c].extend(moving_stack)

        # 이동한 모든 숫자의 좌표 갱신
        for x in moving_stack:
            nums_idx[x] = (max_r, max_c)


# 출력 형식 (빈 칸이면 None 또는 문제 요구 출력 형태에 맞춰 조정)
for r in range(n):
    for c in range(n):
        if not grid[r][c]:
            print('None')
        else:
            print(*reversed(grid[r][c]))