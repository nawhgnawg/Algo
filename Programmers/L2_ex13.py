# 프로그래머스 - 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

k, d = 2, 4

def solution(k, d):
    answer = 0
    ak = 0
    while ak <= d:
        line = (d ** 2 - ak ** 2) ** 0.5
        print(line)
        answer += int(line) // k + 1

        ak += k

    return answer

print(solution(k, d))