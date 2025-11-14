# 프로그래머스 Level 2 - 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def time_convert(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    today = time_convert(today)
    terms_dict = {}

    for term in terms:
        privacy, month = term.split(" ")
        terms_dict[privacy] = int(month) * 28

    for idx, privacy in enumerate(privacies):
        start, name = privacy.split()
        end = time_convert(start) + terms_dict[name]
        if end <= today:
            answer.append(idx + 1)

    return answer

today, terms, privacies = "2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]    # result [1, 3]
print(solution(today, terms, privacies))