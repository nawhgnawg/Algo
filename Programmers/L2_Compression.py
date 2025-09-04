# 프로그래머스 Level 2 - 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684


# 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 5. 단계 2로 돌아간다.

# def solution(msg):
#     answer = []
#     words = {'A': 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
#              "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
#              "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
#     now_msg = ""    # 현재 문자열
#     num = 27        # 다음 색인 번호
#     for i in range(len(msg)):    # KAKAO -> K(11) -> KA(27 등록) -> A(1) -> AK(28 등록) -> KA(27) -> KAO(29 등록) -> O(15)
#         now_msg += msg[i]
#         print(now_msg)
#         if now_msg in words:   # 단어가 사전에 있다면 색인 번호 출력
#             answer.append(words[now_msg])
#         else:   # 없다면 사전에 추가
#             words[now_msg] = num
#             now_msg = ""
#             i -= 1
#
#     return answer

def solution(msg):
    # 1. 사전 초기화
    words = {chr(i + 64): i for i in range(1, 27)}  # A=1 ~ Z=26
    num = 27
    answer = []
    i = 0

    while i < len(msg):
        # 2. 현재 입력과 일치하는 가장 긴 문자열 w 찾기
        w = msg[i]
        j = i + 1
        while j <= len(msg) and msg[i:j] in words:
            w = msg[i:j]
            j += 1

        # 3. w의 색인 번호 출력
        answer.append(words[w])

        # 4. 처리되지 않은 글자가 남아있으면 w+c를 사전에 등록
        if j <= len(msg):
            words[msg[i:j]] = num
            num += 1

        # 5. 입력에서 w 제거 (인덱스 이동)
        i += len(w)

    return answer

msg = "KAKAO"                          # return [11, 1, 27, 15]
# msg = "TOBEORNOTTOBEORTOBEORNOT"       # return [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# msg = "ABABABABABABABAB"               # return [1, 2, 27, 29, 28, 31, 30]
print(solution(msg))