# 프로그래머스 Level 2 - 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.

# dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
# dirs의 길이는 500 이하의 자연수입니다.

def solution(dirs):
    x, y = 0, 0
    visited = set()
    # 1. dx, dy 로 표현 말고 -> UDRL 이 정해져 있기때문에 딕셔너리로 표현
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    # 탐색
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x + dx, y + dy

        # 경계 확인
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # (현재 위치, 다음 위치) 를 정렬해서 저장
            if (x, y) < (nx, ny):
                visited.add(((x, y), (nx, ny)))
            else:
                visited.add(((nx, ny), (x, y)))

            x, y = nx, ny  # 실제 이동

    return len(visited)

dirs = "ULURRDLLU"      # return 7
# dirs = "LULLLLLLU"      # return 7
print(solution(dirs))
