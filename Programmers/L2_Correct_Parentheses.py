# 프로그래머스 Level 2 - 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:  # ")" 가 오는 경우
            # 처음에 ")" 가 오는 경우
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []


s = "()()"      # return true
# s = "(())()"    # return true
# s = ")()("      # return false
print(solution(s))