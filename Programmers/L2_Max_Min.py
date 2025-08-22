# 프로그래머스 Level2 - 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

# min()과 max()를 문자열에 적용하면 사전식(lexicographical) 비교를 하게 된다.
# "10" < "2" 처럼 나옴

def solution(s):
    numbers = list(map(int, s.split(' ')))
    answer = str(min(numbers)) + ' ' + str(max(numbers))
    return answer

print(solution("-1 -2 -3 -4"))