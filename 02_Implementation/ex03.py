# 왕실의 나이트
start = 'a2'

def solution(start):
    result = 0

    row = int(ord(start[0]) - int(ord('a'))) + 1  # 가로
    column = int(start[1])      # 세로

    # 나이트가 갈 수 있는 step
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        # 해당 위치로 이동이 가능하다면 카운트 증가
        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    return result

print(solution(start))