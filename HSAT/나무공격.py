# Level 2 - 나무 공격
# https://exam.hyundai-ngv.com/app/assessment/index.html?xid=493170&xsrfToken=SKsO3N6zHBSOlGGvXtPacfYHlXFcXTjS&testType=practice

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 2번의 공격 입력 (1-based index이므로 -1 처리)
attacks = []
for _ in range(2):
    s, e = map(int, input().split())
    attacks.append((s - 1, e - 1))

# 1. 2번의 공격 시뮬레이션
for start_row, end_row in attacks:
    # 공격 범위에 해당하는 각 행에 대해
    for r in range(start_row, end_row + 1):
        # 왼쪽부터 오른쪽으로 훑으면서 가장 처음 만나는 요정 파괴
        for c in range(m):
            if grid[r][c] == 1:
                grid[r][c] = 0  # 요정 파괴
                break  # 한 행당 한 마리만 파괴되므로 즉시 다음 행으로 넘어감

print(sum([sum(row) for row in grid]))

# n, m = map(int, input().split())

# grid = [list(map(int, input().split())) for _ in range(n)]

# attacks = [tuple(map(int, input().split())) for _ in range(2)]

# # 왼쪽에서 오른쪽 이동
# for s, e in attacks:
#     attack = [c for c in range(s - 1, e)]
#     for i in range(m):
#         col = [grid[j][i] for j in range(n)]
#         for k in range(s - 1, e):
#             # 이미 한번 만났던 요정이면 넘어감
#             if k not in attack:
#                 continue
#             if col[k] == 1:
#                 col[k] = 0
#                 attack[attack.index(k)] = -1

#         for j in range(n):
#             grid[j][i] = col[j]


# print(sum([sum(row) for row in grid)])