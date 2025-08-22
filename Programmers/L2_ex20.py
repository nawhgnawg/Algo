# 프로그래머스 - k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

n = 437674
k = 3

def solution(n, k):
    answer = -1
    # k진수로 바꾸기
    c_num = []
    while n > k:
        c_num.append(n % k)
        n //= k
    c_num.append(n)
    print(c_num)

    # 변환된 숫자를 0을 기준으로 나눈다.
    return answer

print(solution(n, k))