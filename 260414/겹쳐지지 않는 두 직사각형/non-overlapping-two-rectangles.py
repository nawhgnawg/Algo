n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 직사각형의 좌표와 합을 저장할 리스트
rectangles = []

# 1. 가능한 모든 직사각형을 찾아서 리스트에 추가
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                # (r1, c1)부터 (r2, c2)까지의 합 구하기
                current_sum = 0
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        current_sum += grid[i][j]
                
                # 시작점, 끝점, 합을 리스트에 추가
                rectangles.append((r1, c1, r2, c2, current_sum))

max_total = -float('inf')
# max_total = 0

# 2. 저장해둔 직사각형들 중 2개를 뽑아 비교
for i in range(len(rectangles)):
    for j in range(i + 1, len(rectangles)):
        r1, c1, r2, c2, sum1 = rectangles[i]
        r3, c3, r4, c4, sum2 = rectangles[j]

        # 두 직사각형이 겹치지 않는지 확인
        # r2 < r3: 1번이 2번보다 위에 있음
        # r4 < r1: 1번이 2번보다 아래쪽에 있음 
        # c2 < c3: 1번이 2번보다 왼쪽에 있음
        # c4 < c1: 1번이 2번보다 오른쪽에 있음
        if r2 < r3 or r4 < r1 or c2 < c3 or c4 < c1:
            max_total = max(max_total, sum1 + sum2)

print(max_total)

        