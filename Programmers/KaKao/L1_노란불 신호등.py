# 프로그래머스 Level 1 - 노란불 신호등
# https://school.programmers.co.kr/learn/courses/30/lessons/468371

import math

# 최소공배수를 구하는 함수
def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solution(signals):

    # 1. 각 신호등의 1사이클 시간(초록 + 노랑 + 빨강) 계산
    cycles = [sum(sig) for sig in signals]

    # 2. 모든 신호등 주기의 최소공배수(최대 탐색 시간) 구하기
    max_time = 1
    for c in cycles:
        max_time = get_lcm(max_time, c)

    # 3. 1초부터 최소공배수(max_time)까지 탐색
    # 시간은 1초부터 시작하므로 편의상 t를 0부터 시작하여 수식(%) 계산에 사용
    for t in range(max_time):
        all_yellow = True

        for i in range(len(signals)):
            g, y, r = signals[i]
            c = cycles[i]

            # 현재 시간이 해당 신호등 주기의 어느 시점인지 계산
            current_time = t % c

            # 노란불이 켜져있는 시간대인지 확인
            if not (g <= current_time < g + y):
                all_yellow = False
                break

        # 모든 신호등이 노란불 조건을 만족했다면 현재 시간(t + 1) 리턴
        if all_yellow:
            return t + 1

    # 최소공배수 시간까지 모두 노란불인 경우가 없다면 영원히 만나지 않음
    return -1