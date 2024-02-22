# 프로그래머스 - 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

# 1차
def solution1(sizes):
    max_value = 0
    min_value = 0
    for size in sizes:
        a, b = size[0], size[1]
        if a > max_value:
            max_value = a
            print(max_value)
        if b > min_value:
            min_value = b

    return max_value * min_value

print(solution1(sizes))