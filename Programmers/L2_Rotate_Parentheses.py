# 프로그래머스 Level 2 - 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

# s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

# 문자열을 i칸만큼 왼쪽 회전 (즉, s[i:] + s[:i])
# 회전한 문자열이 올바른 괄호 문자열인지 확인
#   스택(Stack) 자료구조를 활용
#   여는 괄호((, [, {) → push
#   닫는 괄호(), ], }) → 스택 top과 매칭되는지 확인 → 아니면 False
#   끝까지 갔을 때 스택이 비어있어야 올바른 괄호 문자열
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":   # 여는 괄호면 push
            stack.append(char)
        else:   # 닫는 괄호면 매칭 검사
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack   # 스택이 비어야 올바른 문자열


def solution(s):
    n = len(s)
    count = 0
    for i in range(n):
        rotated = s[i:] + s[:i]  # 왼쪽 회전
        if is_valid(rotated):
            count += 1
    return count


s = "[](){}"    # return 3
# s = "}]()[{"    # return 2
# s = "[)(]"      # return 0
# s = "}}}"       # return 0
print(solution(s))