# 프로그래머스 Level 4 - 징검 다리
# https://school.programmers.co.kr/learn/courses/30/lessons/43236

# 이분 탐색(Binary Search) + 탐욕법(Greedy)

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 최소 거리 후보
        removed = 0
        prev = 0  # 이전 돌 위치
        min_dist = float('inf')

        for rock in rocks:
            if rock - prev < mid:
                removed += 1  # 돌 제거
            else:
                min_dist = min(min_dist, rock - prev)
                prev = rock

        if removed > n:  # 너무 많이 제거 → mid 줄여야 함
            right = mid - 1
        else:  # mid 가능 → 더 크게 해봄
            answer = min_dist
            left = mid + 1

    return answer

distance, rocks, n = 25, [2, 14, 11, 21, 17], 2     # return 4
print(solution(distance, rocks, n))

