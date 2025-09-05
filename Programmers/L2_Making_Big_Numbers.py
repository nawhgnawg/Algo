# 프로그래머스 Level 2 - 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

def solution(number, k):
    stack = []
    for digit in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작으면 pop
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 아직 k개를 다 제거하지 않았다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

number, k = "1924", 2       # return 94
# number, k = "1231234", 3       # return 3234
# number, k = "4177252841", 4       # return 775841

print(solution(number, k))