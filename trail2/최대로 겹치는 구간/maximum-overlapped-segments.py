n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 1. 음수 좌표를 처리하기 위해 +100 오프셋 적용
OFFSET = 100
MAX_R = 200

# 겹치는 횟수를 기록할 도화지 배열 (0으로 초기화)
# -100부터 100까지 총 201개의 점이 있으므로 여유 있게 크기를 잡습니다.
checked = [0] * (MAX_R + 1)

# 2. 각 선분을 꺼내서 배열에 색칠하기
for x1, x2 in segments:
    # 인덱스 에러를 막기 위해 모든 좌표에 100을 더함
    x1 += OFFSET
    x2 += OFFSET
    
    # 끝점(x2)에서 닿는 것은 겹치는 게 아니므로, x2 - 1 까지만 순회!
    for i in range(x1, x2):
        checked[i] += 1

# 3. 배열에 기록된 값 중 가장 많이 겹친(가장 값이 큰) 횟수 출력
print(max(checked))