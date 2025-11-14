# 프로그래머스 Level 2 - 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2

    # 총합이 홀수면 절대 같게 만들 수 없음
    if total % 2 == 1:
        return -1

    target = total // 2
    limit = len(q1) * 3  # 무한 루프 방지용 (최대 이동 횟수)

    i = 0
    while i < limit:
        if sum1 == target:
            return i
        elif sum1 > target:
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)
        else:
            x = q2.popleft()
            sum2 -= x
            sum1 += x
            q1.append(x)
        i += 1

    return -1


queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]      # return 2
# queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]     # return 7
# queue1, queue2 = [1, 1], [1, 5]                  # return -1
print(solution(queue1, queue2))