n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 모든 위치에서의 1x3 격자 합을 미리 구해둡니다. O(N^2)
sums = [[0] * (n - 2) for _ in range(n)]
for i in range(n):
    for j in range(n - 2):
        sums[i][j] = grid[i][j] + grid[i][j+1] + grid[i][j+2]

answer = 0

# 케이스 1: 두 격자가 '다른 행'에 있을 때
if n >= 2:
    # 각 행에서 가장 큰 1x3 합만 뽑아냅니다.
    row_maxes = [max(row) for row in sums]
    # 내림차순 정렬해서 1등과 2등을 더합니다.
    row_maxes.sort(reverse=True)
    answer = max(answer, row_maxes[0] + row_maxes[1])

# 케이스 2: 두 격자가 '같은 행'에 있을 때
for i in range(n):
    max_left = 0
    # 오른쪽 격자의 시작점 j는 최소 3부터 시작해야 왼쪽에 격자가 들어갈 자리가 있습니다.
    for j in range(3, n - 2):
        # 방금 배운 그 기술! j에서 3칸 떨어진(절대 안 겹치는) 왼쪽 중 가장 컸던 값을 기억합니다.
        max_left = max(max_left, sums[i][j - 3])
        
        # [왼쪽에서 젤 컸던 값] + [현재 나의 값]
        answer = max(answer, max_left + sums[i][j])

print(answer)