# 프로그래머스 Level 3 - 산 모양 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/258705

# DP(동적 계획법)
# n개의 마름모(기본 타일)를 왼쪽부터 오른쪽으로 이어붙인 산 모양을 만든다.
# 각 칸 위에는 삼각형 타일(위쪽 삼각형)을 붙일 수도 있다 (tops[i] == 1이면 가능).
# 타일을 규칙에 맞게 배치하는 모든 경우의 수를 구해야 한다.
# 결과는 10007로 나눈 나머지를 반환한다.

def solution(n, tops):
    answer = 0
    return answer

n, tops = 4, [1, 1, 0, 1]       # return 149
# n, tops = 2, [0, 1]             # return 11
# n, tops = 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       # return 7704
print(solution(n, tops))