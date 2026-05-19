n = int(input())
segments = []
for _ in range(n):
    left, right = map(int, input().split())
    segments.append((left, right))

answer = 0

# i, j, k 는 지울 선분 3개의 인덱스
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            # 1. i, j, k의 선분들을 제외한 남은 선분들만 모은다.
            remaining = []
            for idx in range(n):
                if idx not in (i, j, k):
                    remaining.append(segments[idx])

            # 2. 남은 선분들끼리 서로 겹치는지 확인
            is_overlapping = False

            for line1 in range(len(remaining)):
                for line2 in range(line1 + 1, len(remaining)):
                    left1, right1 = remaining[line1]
                    left2, right2 = remaining[line2]

                    # 겹치는 조건: A의 끝점이 B의 시작점보다 크거나 같고, A의 시작점이 B의 끝점보다 작거나 같음
                    if right1 >= left2 and left1 <= right2:
                        is_overlapping = True
                        break
                    
                if is_overlapping:
                    break
            
            if not is_overlapping:
                answer += 1

print(answer)

        