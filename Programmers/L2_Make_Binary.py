# 프로그래머스 Level 2 - 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

# "01110" -> "111" -> "11"
# "11" -> "11" -> "10"
# "10" -> "1" -> "1"
# 3회차를 진행하는동안 3개의 0을 제거 -> return [3, 3]
# 0을 제거한 수가 "1" 이 되어야함

def solution(s):
    binary_num = s
    temp = ""

    zero_count = 0
    level = 0

    while True:
        for b in binary_num:
            # 1이면 추가
            if b == "1":
                temp += "1"
            # 0이면 제거 후, 제거한 수 1 추가
            elif b == "0":
                zero_count += 1
        # "111" -> "11" 처리
        binary_num = bin(len(temp))[2:]
        level += 1

        if temp == "1":
            break

        temp = ""

    return [level, zero_count]


s = "110010101001"      # [3, 8]
# s = "01110"             # [3, 3]
# s = "1111111"           # [4, 1]
print(solution(s))