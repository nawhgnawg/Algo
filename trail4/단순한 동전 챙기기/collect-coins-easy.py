from itertools import combinations

n = int(input())
grid = [list(input()) for _ in range(n)]

# 상하좌우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

numbers = []

start_x, start_y = 0, 0
end_x, end_y = 0, 0

# 적혀 있는 숫자 찾기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_x, start_y = i, j
        elif grid[i][j] == 'E':
            end_x, end_y = i, j
        elif grid[i][j].isdigit():
            numbers.append((int(grid[i][j]), i, j))

# 3개 이하면 -1 출력
if len(numbers) < 3:
    print(-1)
    exit()

# 2. 동전 정렬하기
# 문제에서 "오름차순으로 방문"
numbers.sort()

# 두 점 사이의 거리를 구하는 함수 (맨해튼 거리)
def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

min_distance = float('inf')


# 3. 3개만 뽑아서 거리 계산하기
# coins가 이미 오름차순 정렬되어 있으므로, 뽑힌 c1, c2, c3도 무조건 오름차순입니다.
for c1, c2, c3 in combinations(numbers, 3):

    # 1) S -> 첫 번째 동전
    dist1 = get_dist(start_x, start_y, c1[1], c1[2])
    # 2) 첫 번째 동전 -> 두 번째 동전
    dist2 = get_dist(c1[1], c1[2], c2[1], c2[2])
    # 3) 두 번째 동전 -> 세 번째 동전
    dist3 = get_dist(c2[1], c2[2], c3[1], c3[2])
    # 4) 세 번째 동전 -> E
    dist4 = get_dist(c3[1], c3[2], end_x, end_y)

    total_dist = dist1 + dist2 + dist3 + dist4

    # 최솟값 갱신
    min_distance = min(min_distance, total_dist)


# 만약 최솟값이 갱신되었다면 출력, 아니면 -1 출력
if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)


