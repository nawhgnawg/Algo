n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 각 숫자(1 ~ N*N)의 현재 좌표를 O(1)로 조회하기 위한 배열
pos = [(0, 0)] * (n * n + 1)
for r in range(n):
  for c in range(n):
    pos[grid[r][c]] = (r, c)

# 8방향 벡터 (상좌, 상, 상우, 좌, 우, 하좌, 하, 하우)
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
  for num in range(1, n * n + 1):
    r, c = pos[num]

    max_val = -1
    max_r, max_c = -1, -1

    for i in range(8):
      nr, nc = r + dr[i], c + dc[i]
      if 0 <= nr < n and 0 <= nc < n:
        if grid[nr][nc] > max_val:
          max_val = grid[nr][nc]
          max_r, max_c = nr, nc

    # 인접한 칸이 존재할 때만 교환 및 위치 정보 갱신
    if max_r != -1:
      other_num = grid[max_r][max_c]

      # 격자 값 교환
      grid[r][c], grid[max_r][max_c] = grid[max_r][max_c], grid[r][c]

      # 두 숫자의 위치 기록 동기화
      pos[num] = (max_r, max_c)
      pos[other_num] = (r, c)

for row in grid:
  print(*row)


# def find_rc(num):
#     for r in range(n):
#         for c in range(n):
#             if grid[r][c] == num:
#                 return r, c

# # 8방향 백터
# dr = [-1, -1, -1, 0, 0, 1, 1, 1]
# dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# for _ in range(m):
#     for num in range(1, n * n + 1):
#         r, c = find_rc(num)

#         max_val = -1
#         max_r, max_c = 0, 0

#         for i in range(8):
#             nr, nc = r + dr[i], c + dc[i]
#             if 0 <= nr < n and 0 <= nc < n:
#                 if grid[nr][nc] > max_val:
#                     max_val = grid[nr][nc]
#                     max_r, max_c = nr, nc

#         # 특정 조건에 맞춰 교환
#         grid[r][c], grid[max_r][max_c] = grid[max_r][max_c], grid[r][c]

# for row in grid:
#     print(*row)
