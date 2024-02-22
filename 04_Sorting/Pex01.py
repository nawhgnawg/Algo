# 프로그래머스 - K 번째 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 1차
def solution1(array, commands):
    result = []
    for command in commands:
        new_array = []
        for i in range(command[0] - 1, command[1]):
            new_array.append(array[i])
        new_array.sort()
        result.append(new_array[command[2] - 1])

    return result

print(solution1(array, commands))