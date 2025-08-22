# 프로그래머스 - 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

from collections import deque
def solution(k, dungeons):
    answer = -1
    q = deque()
    q.append((k, []))

    while q:
        k, route = q.popleft()
        for i in range(len(dungeons)):
            a, b = dungeons[i]
            if k >= a and i not in route:
                temp = route + [i]
                q.append((k - b, temp))
            else:
                answer = max(answer, len(route))

    return answer

print(solution(k, dungeons))