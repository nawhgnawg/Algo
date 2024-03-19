# 2023 KAKAO BLIND RECRUITMENT
# 프로그래머스 - 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

# 첫번째
import re
def solution1(today, terms, privacies):
    answer = []
    sp_terms = []
    for te in terms:
        a, b = te.split(" ")
        sp_terms.append(a)
        sp_terms.append(b)

    s_today = today.split(".")
    count = 1
    for privaciy in privacies:
        y, m, d, t = re.split("[. ]", privaciy)
        y = int(y); m = int(m); d = int(d)
        term_index = sp_terms.index(t) + 1
        p_m = m + int(sp_terms[term_index])
        # 일이 1일일때
        if d == 1:
            # 12가 넘으면
            if p_m > 12:
                y += 1
                p_m -= 13
                d = 28
            # 12 안 넘으면
            else:
                p_m -= 1
                d = 28
        # 일이 1이 아닐때
        else:
            # 합이 12가 넘을 때
            if p_m > 12:
                y += 1
                p_m -= 12
                d -= 1
            # 합이 12가 안 넘을 때
            else:
                d -= 1
        # 유효기간과 비교
        # 유효기간보다 작으면
        if y < int(s_today[0]):
            answer.append(count)
        else:
            if p_m < int(s_today[1]):
                answer.append(count)
            else:
                if d < int(s_today[2]):
                    answer.append(count)
        count += 1
    return answer

# 2번째
def time_convert(t):
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution2(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []

    for term in terms:
        name, period = term.split()
        term_dict[name] = int(period) * 28

    for idx, privacy in enumerate(privacies):
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today:
            answer.append(idx + 1)

    return answer

print(solution2(today, terms, privacies))