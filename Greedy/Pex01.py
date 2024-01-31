# 프로그래머스 - 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
n = 5
lost = [2, 4]
reserve = [1, 3, 5]


# 1차 - 예외 케이스
def solution1(n, lost, reserve):
    answer = 0
    answer = answer + n - len(lost)

    for i in range(len(reserve)):
        if reserve[i] in lost:
            reserve.remove[i]
            answer += 1

    for i in range(len(reserve)):
        if reserve[i] - 1 in lost:
            lost.remove(reserve[i] - 1)
            answer += 1
        elif reserve[i] + 1 in lost:
            lost.remove(reserve[i] + 1)
            answer += 1

    return answer


# 2차 - 런타임 에러 - list의 remove()는 O(n)
def solution2(n, lost, reserve):
    _lost = []
    _reserve = []
    # lost와 reserve에 중복되는 학생 구분
    for num in lost:
        if num not in reserve:
            _lost.append(num)

    for num in reserve:
        if num not in lost:
            _reserve.append(num)

    for num in _reserve:
        if num - 1 in _lost:
            _lost.remove(num - 1)
        elif num + 1 in lost:
            _lost.remove(num + 1)

    return n - len(_lost)


# 3차 - set의 remove()는 O(1)
def solution3(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    for num in _reserve:
        if num - 1 in _lost:
            _lost.remove(num - 1)
        elif num + 1 in _lost:
            _lost.remove(num + 1)

    return n - len(_lost)


# 4차 - 다른사람 풀이
def otherSolution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

print(solution3(n, lost, reserve))