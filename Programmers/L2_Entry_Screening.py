# 프로그래머스 Level 3 - 입국 심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 이분 탐색(Binary Search)

def solution(n, times):
    left, right = 1, max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)  # mid분 동안 심사한 총 인원

        if total >= n:  # n명 이상 심사 가능
            answer = mid
            right = mid - 1  # 더 짧은 시간 탐색
        else:
            left = mid + 1  # 시간이 부족 → 더 늘림

    return answer

n, times = 6, [7, 10]       # return 28
print(solution(n, times))