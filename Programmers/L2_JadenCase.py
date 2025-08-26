# 프로그래머스 Level 2 - JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    answer = ''
    split_s = s.split(" ")
    for word in split_s:
        # 공백만 있는 경우 그대로 공백 추가 ****
        if word == "":
            answer += " "
            continue
        # 첫 문자가 숫자일 때 -> 숫자 + 나머지 모두 소문자
        if word[0].isdigit():
            answer += word[0]
            answer += word[1:].lower()
        # 첫 문자가 대문자일때 -> 첫 문자만 대문자, 나머지 모두 소문자
        elif word[0].isupper():
            answer += word[0]
            answer += word.lower()[1:]
        # 첫 문자가 소문자일때 -> 첫 문자만 대문자, 나머지 모두 소문자
        elif word[0].islower():
            answer += word[0].upper()
            answer += word.lower()[1:]
        answer += " "
    return answer[:len(answer) - 1]

print(solution("3people unFollowed me"))