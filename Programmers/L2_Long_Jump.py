# 프로그래머스 Level 2 - 멀리 뛰기
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다.
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내,
# 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.

# n은 1 이상, 2000 이하인 정수입니다.

def solution(n):
    MOD = 1234567
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

n = 4       # return 5
# n = 3       # return 3
print(solution(n))