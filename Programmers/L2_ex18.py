# 프로그래머스 - 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

# 1차 - 그리디
from collections import Counter
def solution(k, tangerine):
    C = Counter(tangerine)
    a = set()
    for key, val in C.most_common():
        while k > 0:
            k -= 1
            C[key] -= 1
            a.add(key)
        if k == 0:
            return len(a)
    return len(a)

# 2차
def solution2(k, tangerine):
    answer = 0
    C = Counter(tangerine)
    a = set()
    for key, val in C.most_common():
        k -= val
        answer += 1
        if k <= 0:
            return answer

    return answer


print(solution2(k, tangerine))