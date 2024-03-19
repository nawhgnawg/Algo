# 프로그래머스 - 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

answers = [1,3,2,4,2]

# 1차 - 런타임 에러
def solution1(answers):
    result = []
    # 각 수포자별로 맞춘 개수
    p = [0] * 3
    ps = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    n = len(answers)
    p1_n = len(ps[0]) // n if len(ps[0]) % n == 0 else len(ps[0]) // n + 1
    p2_n = len(ps[1]) // n if len(ps[1]) % n == 0 else len(ps[1]) // n + 1
    p3_n = len(ps[2]) // n if len(ps[2]) % n == 0 else len(ps[2]) // n + 1

    ps[0] *= p1_n
    ps[1] *= p2_n
    ps[2] *= p3_n

    for i in range(len(ps)):
        for j in range(len(answers)):
            if ps[i][j] == answers[j]:
                p[i] += 1

    max_val = max(p)
    for i in range(len(p)):
        if p[i] >= max_val:
            result.append(i + 1)

    return result

print(solution1(answers))