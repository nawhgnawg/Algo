# 시각
# 유형 - 완전탐색 (가능한 경우의 수를 모두 검사)
n = 5

def solution(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    return count

print(solution(n))