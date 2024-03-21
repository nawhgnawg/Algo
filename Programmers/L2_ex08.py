# 프로그래머스 - 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

numbers = [9, 1, 5, 3, 6, 2]

# 1차 - 시간 초과
def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        M = 1
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                M = max(M, numbers[j])
                answer.append(M)
                break
        if M == 1:
            answer.append(-1)
    return answer


# 2차
# numbers를 탐색하며, 스택이 내림차순이 되도록 스택을 저장한다.
from collections import deque
def solution2(numbers):
    length = len(numbers)       # numbers의 길이 (6)
    answer = [-1] * length      # [-1, -1, ... , -1]
    stk = deque([])
    for i in range(length):
        value = numbers[i]
        while stk and numbers[stk[-1]] < value:
            answer[stk[-1]] = value
            stk.pop()
        stk.append(i)
    return answer

# 3차
def solution3(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]

        stack.append(i)

    return answer

print(solution2(numbers))