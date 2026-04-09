n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

happy_count = 0

# 주어진 1차열 수열이 행복한 수열인지 판별하는 함수
def is_happy(seq):
    max_count = 1       # 가장 길게 연속된 횟수
    current_count = 1   # 현재 연속되고 있는 횟수

    for i in range(1, n):
        if seq[i] == seq[i - 1]:    # 바로 앞 숫자와 같다면
            current_count += 1
            max_count = max(max_count, current_count)   
        else:                   # 숫자가 달라져서 연속이 끊겼다면
            current_count = 1   # 다시 1부터 세기 시작

    return max_count >= m

# 1. 모든 가로줄(행) 검사
for i in range(n):
    row_seq = grid[i]
    if is_happy(row_seq):
        happy_count += 1

# 2. 모든 세로줄(열) 검사
for i in range(n):
    col_seq = [grid[i][j] for j in range(n)]
    if is_happy(col_seq):
        happy_count += 1

print(happy_count)