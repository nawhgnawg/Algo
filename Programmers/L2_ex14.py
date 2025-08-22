# 프로그래머스 - 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

topping = [1, 2, 1, 3, 1, 4, 1, 2]

from collections import Counter
def solution(topping):
    answer = 0
    C = Counter(topping)
    s = set()
    for t in topping:
        C[t] -= 1
        if C[t] == 0:
            del C[t]
        s.add(t)
        if len(C.keys()) == len(s):
            answer += 1
    return answer


print(solution(topping))