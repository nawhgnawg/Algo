# 2019 - 상반기 LINE 인턴 채용 코딩테스트 문제
# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test
from collections import deque


# 연인 코니와 브라운은 광활한 들판에서 '나 잡아 봐라' 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, ...이다.

# 브라운은 현재 위치 B에서 다음 순간 B - 1, B + 1, 2 * B 중 하나로 움직일 수 있다.

# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.


# 1. 1초부터 경우의 수를 생각해본다.
# 2. 모든 경우의 수를 다 봐야할 것 같다. -> BFS, DFS
# 3. 시간에 따른 위치가 마주잡이로 변하는 구나 -> Dictionary
#   3-1. 즉 배열에 Dictionary를 넣어주면 좋다. [예) [0] 초에 위치할 수 있었던 곳들] -> [{}, {}, {}..]


def catch_me(cony_loc, brown_loc):
    time = 0

    queue = deque()
    queue.append((brown_loc, 0))

    # x의 위치에 도달한 시간들의 모음 딕셔너리
    # visited[3] = {5: True, 9: True} -> 3의 위치에 도달한 시간들이 5초랑 9초 였다는 것이다.
    visited = [{} for _ in range(200_001)]  # 20만개

    # 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
    # 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
    while cony_loc <= 200_000:
        cony_loc += time    # 코니는 시간을 더해준다.

        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):  # 왜 while queue: 를 안쓰고 for 문을 사용할까?
            current_position, current_time = queue.popleft()    # brown_loc, 0

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 200_000:
                visited[new_position][new_time] = True  # visited의 new_position 인덱스에 new_time이라는 키 값을 True로 만든다.
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200_000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200_000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1

    return time


def solution(c_start, b_start):
    answer = 0
    # 코니는 일정한 값이 나옴
    c_distance = c_start
    b_distance = b_start
    time = 1

    while answer < 5:
        answer += 1
        c_distance = c_distance + time     # 코니는 초마다 1
        print(c_distance)
        b_distance = b_distance - 1
        print(b_distance)
        if b_distance == c_distance:
            return answer
        b_distance = b_distance + 1
        print(b_distance)
        if b_distance == c_distance:
            return answer
        b_distance = b_distance * 2
        print(b_distance)
        if b_distance == c_distance:
            return answer

        time += 1

# 11 2 -> 5
cony_loc, brown_loc = map(int, input().split())    # 코니와 브라운의 시작 위치
print(catch_me(cony_loc, brown_loc))
# print(solution(C, B))
