# 프로그래머스 Level 2 - 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

# n은 1,000,000 이하의 자연수 입니다.
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

def solution(n):
    answer = 0
    # 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    # 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    binary_n = bin(n)[2:]               # 78 -> 1001110
    count_one = binary_n.count("1")     # 1001110 -> 64 + 8 + 4 + 2 -> 4개

    # 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
    # n + 1 ~ 1,000,000 까지
    for i in range(n + 1, 1_000_001):
        binary_i = bin(i)[2:]
        if count_one == binary_i.count("1"):
            answer = i
            break

    return answer


n = 78      # return 83
# n = 15      # return 23
print(solution(n))