# 프로그래머스 Level 2 - 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

# [A, B, C, D, E, F] -> 0(A) -> [C, D, E, F, A, B] -> 5번째
# 1: 1, 2: 1, 3: 9, 4: 1, 5: 1, 6: 1
from collections import deque
def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (우선순위, 인덱스)
    sorted_priorities = sorted(priorities, reverse=True)  # 높은 순서대로
    order = 0
    while queue:
        cur = queue.popleft()
        # 지금 처리할 차례의 "최고 우선순위"와 비교
        if cur[0] < sorted_priorities[order]:
            queue.append(cur)
        else:
            order += 1
            if cur[1] == location:  # 찾던 프로세스 실행됨
                return order

priorities, location = [2, 1, 3, 2], 2                # return 1
# priorities, location = [1, 1, 9, 1, 1, 1], 0          # return 5
print(solution(priorities, location))