n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# K는 1부터 시작하므로 인덱스 계산을 위해 0-based로 변환
start_col = k - 1
end_col = start_col + m

# 블록이 안착할 최종 행(Row). 초기값은 맨 밑바닥으로 둡니다.
target_row = n - 1

# 위에서부터 아래로 한 줄씩 탐색하며 떨어질 공간을 확인합니다.
for r in range(n):
    collision = False
    
    # 블록이 차지하는 가로 공간 중 하나라도 1이 있는지 확인
    for c in range(start_col, end_col):
        if grid[r][c] == 1:
            collision = True
            break
            
    # 장애물에 부딪혔다면, 그 바로 윗줄(r - 1)에 안착해야 하므로 탐색 종료
    if collision:
        target_row = r - 1
        break

# 찾아낸 최종 위치에 블록(1)을 채워 넣습니다.
for c in range(start_col, end_col):
    grid[target_row][c] = 1

# 완성된 격자 상태를 출력합니다.
for row in grid:
    print(*row)