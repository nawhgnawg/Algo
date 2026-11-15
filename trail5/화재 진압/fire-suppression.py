from bisect import bisect_left

n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# 1. 소방서 위치 정렬 (이분 탐색을 위함)
stations.sort()

max_time = 0

# 2. 각 화재 위치마다 가장 가까운 소방서 찾기
for f in fires:
    # f보다 크거나 같은 첫 번째 소방서의 인덱스 찾기
    idx = bisect_left(stations, f)

    min_dist = float('inf')

    # 바로 오른쪽 소방서와의 거리 비교
    if idx < m:
        min_dist = min(min_dist, abs(stations[idx] - f))
    
    # 바로 왼쪽 소방서와의 거리 비교
    if idx > 0:
        min_dist = min(min_dist, abs(stations[idx - 1] - f))

    # 각 화재 위치에서의 최소 거리 중 최댓값 갱신
    if min_dist > max_time:
        max_time = min_dist

print(max_time)
