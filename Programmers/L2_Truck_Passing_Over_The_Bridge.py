# 프로그래머스 Level 2 - 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 상태 (0=빈 자리)
    current_weight = 0  # 현재 다리에 올라간 트럭 무게 합

    while bridge:
        time += 1
        # 1. 맨 앞 트럭(또는 0) 빠짐
        current_weight -= bridge.popleft()

        if truck_weights:  # 아직 대기 트럭이 있으면
            if current_weight + truck_weights[0] <= weight:
                # 2. 새 트럭 진입
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                # 3. 새 트럭 못 올라가면 0 삽입 (빈 자리 유지)
                bridge.append(0)

    return time

bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]      # return 8
# bridge_length, weight, truck_weights = 100, 100, [10]           # return 101
# bridge_length, weight, truck_weights = 100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]     # return 110
print(solution(bridge_length, weight, truck_weights))