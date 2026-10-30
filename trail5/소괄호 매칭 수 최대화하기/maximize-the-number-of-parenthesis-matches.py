import sys
from functools import cmp_to_key

input = sys.stdin.readline

n = int(input())
strings = [input().strip() for _ in range(n)]

# 두 문자열을 결합했을 때의 점수를 계산하는 함수
def calc_score(s):
    score = 0
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        else:
            score += open_cnt
    return score

# 두 문자열의 전후 배치를 비교하는 커스텀 비교 함수
def compare(s1, s2):
    score_12 = calc_score(s1 + s2)
    score_21 = calc_score(s2 + s1)
    
    # 더 큰 점수를 만드는 순서가 앞으로 오도록 설정
    if score_12 > score_21:
        return -1  # s1이 s2보다 앞에 와야 함
    elif score_12 < score_21:
        return 1   # s2가 s1보다 앞에 와야 함
    else:
        return 0

# cmp_to_key를 이용해 최적의 순서로 정렬
strings.sort(key=cmp_to_key(compare))

# 정렬된 문자열들을 모두 이어붙인 후 최종 점수 계산
final_str = ''.join(strings)
print(calc_score(final_str))