from bisect import bisect_left

n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# O(N + M) - 투 포인터 이용
# 1. 두 배열 모두 오름차순 정렬
fires.sort()
stations.sort()

max_time = 0
j = 0   # 소방서 포인터를 관리하는 변수

# 2. 화재 위치를 순회하며 투 포인터 적용
for i in range(n):
    # 현재 소방서(j)보다 다음 소방서(j+1)가 화재(fires[i])에 더 가깝거나 같으면 j를 전진시킴
    while j + 1 < m and abs(stations[j + 1] - fires[i]) <= abs(stations[j] - fires[i]):
        j += 1

    # 멈춘 시점의 stations[j]가 가장 가까운 소방서이므로 거리 계산
    dist = abs(stations[j] - fires[i])
    if dist > max_time:
        max_time = dist

print(max_time)


# O(NlogM) - bisect 이용
# # 1. 소방서 위치 정렬 (이분 탐색을 위함)
# stations.sort()

# max_time = 0

# # 2. 각 화재 위치마다 가장 가까운 소방서 찾기
# for f in fires:
#     # f보다 크거나 같은 첫 번째 소방서의 인덱스 찾기
#     idx = bisect_left(stations, f)
#     print(f'{f}: {idx}')
#     min_dist = float('inf')

#     # 바로 오른쪽 소방서와의 거리 비교
#     if idx < m:
#         min_dist = min(min_dist, abs(stations[idx] - f))
    
#     # 바로 왼쪽 소방서와의 거리 비교
#     if idx > 0:
#         min_dist = min(min_dist, abs(stations[idx - 1] - f))

#     # 각 화재 위치에서의 최소 거리 중 최댓값 갱신
#     if min_dist > max_time:
#         max_time = min_dist

# print(max_time)
