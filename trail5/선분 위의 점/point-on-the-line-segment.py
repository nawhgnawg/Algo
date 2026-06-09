from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

points.sort()

for s, e in segments:
    # 1. 선분 시작점 이상인 점이 처음 등장하는 인덱스
    left_idx = bisect_left(points, s)

    # 2. 선분 끝점 이하인 점이 끝나는 다음 인덱스
    right_idx = bisect_right(points, e)

    # 3. 두 인덱스 차이가 곧 구간 내에 존재하는 점의 개수
    print(right_idx - left_idx)
