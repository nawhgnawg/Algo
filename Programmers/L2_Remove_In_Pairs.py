# 프로그래머스 - 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973


# 앞에서부터 차례로 보면서 짝이 나오면 없앤다 -> Stack 사용!
# 문자열 합치기(join)는 비싸다 → 반복문 안에서는 피하자
# "짝을 없애는 문제"는 스택으로 풀면 효율적

# def solution(s):
#     temp = list(s)   # 현재 문자열
#     while True:
#         pre_temp = temp.copy()
#         for i in range(len(temp) - 1):
#             if temp[i] == temp[i + 1]:
#                 temp[i] = ""
#                 temp[i + 1] = ""
#                 break
#         if len("".join(temp)) == 0:
#             return 1
#         if "".join(temp) == "".join(pre_temp):
#             return 0
#         temp = list("".join(temp))

def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:  # 짝이 되는 경우
            stack.pop()
        else:
            stack.append(char)           # 스택에 추가
    # 스택이 비어 있으면
    if not stack:
        return 1
    else:
        return 0

# baabaa -> [b] -> [b, a] -> [b] -> [] -> [a] -> []
s = "baabaa"        # return 1      baabaa -> bbaa -> aa -> _
# cdcd -> [c] -> [c, d] -> [c, d, c] -> [c, d, c, d]
# s = "cdcd"          # return 0
print(solution(s))