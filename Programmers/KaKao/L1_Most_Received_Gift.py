# 프로그래머스 Level 1 - 가장 많이 받는 선물
# https://school.programmers.co.kr/learn/courses/30/lessons/258712

# 선물 준 횟수 > 선물 지수(내가 준 선물 - 내가 받은 선물)
# def solution(friends, gifts):
#     answer = 0
#     give = {name: 0 for name in friends}    # 선물 준
#     receive = {name: 0 for name in friends} # 선물 받은
#     score = {name: 0 for name in friends}   # 선물 지수
#
#     # 선물 주고 받은 기록
#     for gift in gifts:
#         giver, receiver = gift.split()
#         give[giver] += 1
#         receive[receiver] += 1
#
#     # 선물 지수 구하기
#     for idx, (g, r) in enumerate(zip(give.values(), receive.values())):
#         score[friends[idx]] = g - r
#
#     for i in range(len(friends)):
#         for j in range(len(friends)):
#             if friends[i] == friends[j]:
#                 continue
#
#     return answer

def solution(friends, gifts):
    n = len(friends)
    # 이름 → 인덱스 매핑
    idx = {name: i for i, name in enumerate(friends)}

    # 선물 주고받기 기록 (2차원 배열)
    table = [[0] * n for _ in range(n)]
    give_count = [0] * n
    receive_count = [0] * n

    # 선물 주고받은 횟수 기록
    for g in gifts:
        giver, receiver = g.split()
        gi, ri = idx[giver], idx[receiver]
        table[gi][ri] += 1
        give_count[gi] += 1
        receive_count[ri] += 1

    # 선물 지수 계산 (준 - 받은)
    score = [give_count[i] - receive_count[i] for i in range(n)]

    # 다음 달 받을 선물 개수 계산
    next_gift = [0] * n
    for i in range(n):
        for j in range(i + 1, n):  # i < j (중복 방지)
            if table[i][j] > table[j][i]:
                next_gift[i] += 1
            elif table[i][j] < table[j][i]:
                next_gift[j] += 1
            else:  # 주고받은 횟수가 같다면 → 선물 지수 비교
                if score[i] > score[j]:
                    next_gift[i] += 1
                elif score[i] < score[j]:
                    next_gift[j] += 1
                # 같으면 아무도 받지 않음

    # 가장 많이 선물 받는 사람의 수
    return max(next_gift)


friends = ["muzi", "ryan", "frodo", "neo"]                          # return 2
gift = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
# friends = ["joy", "brad", "alessandro", "conan", "david"]         # return 4
# gift = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
# friends = ["a", "b", "c"]                                         # return 0
# gift = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gift))