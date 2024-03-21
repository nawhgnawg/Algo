# 프로그래머스 - 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538

x, y = 10, 40
n = 5

# 1차 - BFS
def solution1(x, y, n):
    answer = 0
    if x + n == y:
        return 1

    d2 = y % 2
    d3 = y % 3
    # 2의 배수일 때
    if d2 == 0:
        None
    # 3의 배수일 때

    # 6의 배수일 때
    return answer

# 2차 - BFS
from collections import deque
def solution2(x, y, n):
    visited = [float('inf')] * 1000001
    q = deque([(x, 0)])

    while q:
        num, cnt = q.popleft()
        if num == y:
            return cnt
        if num > 1000000 or visited[num] <= cnt:
            continue
        visited[num] = cnt
        # q에 넣기 [* 2, * 3, + n]
        q.extend([(num * 2, cnt + 1), (num * 3, cnt + 1), (num + n, cnt + 1)])

    return -1

print(solution2(x, y, n))