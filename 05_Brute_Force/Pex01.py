# 프로그래머스 - 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

# 1차
def solution1(sizes):
    row = 0
    col = 0
    for size in sizes:
        a, b = size[0], size[1]
        if a > b:
            row = max(b, row)
            col = max(a, col)
        else:
            row = max(a, row)
            col = max(b, col)

    return row * col

# 2차
def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

print(solution1(sizes))