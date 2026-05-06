n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# cups[0] = 1은 '1번 위치에서 시작한 조약돌'이 현재 0번 인덱스에 있다는 뜻입니다.
cups = [1, 2, 3]

# 1, 2, 3번 각 시작 위치별로 얻은 점수를 저장 (인덱스 편의상 크기를 4로 설정)
scores = [0, 0, 0]

for a, b, c in moves:
    # 1. a번 컵과 b번 컵의 위치를 바꿉니다. (인덱스 조정을 위해 -1)
    cups[a - 1], cups[b - 1] = cups[b - 1], cups[a - 1]
    # 2. c번 위치의 컵을 열었을 때, 그 안에 있는 조약돌의 '원래 시작 번호'를 확인합니다.
    start_pos = cups[c-1]
    # 3. 해당 시작 번호의 점수를 1점 올립니다.
    scores[start_pos - 1] += 1

print(max(scores))