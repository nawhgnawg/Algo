# 프로그래머스 Level 1 - 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    # 1: 매우 비동의, 2: 비동의, 3: 약간 비동의, 4: 모르겠음, 5: 약간 동의, 6: 동의, 7: 매우 동의
    # character = {1: ["R", "T"], 2: ["C", "F"], 3: ["J", "M"], 4: ["A", "N"]}
    points = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i, character in enumerate(survey):
        front, end = character[0], character[1]
        if choices[i] > 4:
            points[end] += choices[i] - 4
        elif choices[i] < 4:
            points[front] = points.get(front) + 4 - choices[i]

    for a, b in ["RT", "CF", "JM", "AN"]:
        if points[a] >= points[b]:
            answer += a
        else:
            answer += b
            
    # if points["R"] >= points["T"]:
    #     answer += "R"
    # elif points["R"] < points["T"]:
    #     answer += "T"
    #
    # if points["C"] >= points["F"]:
    #     answer += "C"
    # elif points["C"] < points["F"]:
    #     answer += "F"
    #
    # if points["J"] >= points["M"]:
    #     answer += "J"
    # elif points["J"] < points["M"]:
    #     answer += "M"
    #
    # if points["A"] >= points["N"]:
    #     answer += "A"
    # elif points["A"] < points["N"]:
    #     answer += "N"

    return answer

# upgrade 버전
# def solution(survey, choices):
#     # 각 성격 유형 점수 초기화
#     score = {ch: 0 for ch in "RTCFJMAN"}
#
#     # 선택지에 따른 점수 (인덱스: 선택 번호)
#     point_table = [3, 2, 1, 0, 1, 2, 3]
#
#     # 점수 계산
#     for s, c in zip(survey, choices):
#         if c < 4:  # 비동의 쪽
#             score[s[0]] += point_table[c - 1]
#         elif c > 4:  # 동의 쪽
#             score[s[1]] += point_table[c - 1]
#
#     # 유형별 비교
#     result = ''
#     for a, b in ['RT', 'CF', 'JM', 'AN']:
#         result += a if score[a] >= score[b] else b
#
#     return result

survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]       # return "TCMA"
# survey, choices = ["TR", "RT", "TR"], [7, 1, 3]                         # return "RCJA"
print(solution(survey, choices))
