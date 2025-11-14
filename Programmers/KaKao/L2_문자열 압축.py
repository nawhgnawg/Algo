# 프로그래머스 Level 2 - 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j: j + step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j: j + step]
                count = 1
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer

s = "aabbaccc"              # return 7
# s = "ababcdcdababcdcd"      # return 9
# s = "abcabcdede"            # return 8
print(solution(s))
