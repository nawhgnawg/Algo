# 프로그래머스 Level 2 - 모음 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다.
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

# "A" -> "AA" -> "AAA" -> "AAAA" -> "AAAAA" -> "AAAAE" -> "AAAAI" -> "AAAAO" -> "AAAAU"
# -> "AAAE" -> "AAAI" -> "AAAO" -> "AAAU"
# -> "AAE" -> "AAI" -> "AAO" -> "AAU"
# -> "AE" -> "AI" -> "AO" -> "AU"
# -> "E" -> "EE" -> "EEE" -> "EEEE" -> "EEEEA" -> "EEEEE" -> "EEEEI" -> "EEEEO" -> "EEEEU"
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dic = []

    def dfs(s):
        if s:               # 빈 문자열 제외하고 사전에 추가
            dic.append(s)
        if len(s) == 5:
            return
        for ch in vowels:   # A→E→I→O→U 순서
            dfs(s + ch)
    
    dfs("")
    return dic.index(word) + 1


word = "AAAAE"      # return 6
# word = "AAAE"       # return 10
# word = "I"          # return 1563
# word = "EIO"        # return 1189
print(solution(word))