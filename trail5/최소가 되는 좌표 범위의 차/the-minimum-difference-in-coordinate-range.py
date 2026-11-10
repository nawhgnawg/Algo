from sortedcontainers import SortedList

n, d = map(int, input().split())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 정렬(Sorting)과 투 포인터(Two Pointer)를 결합하여 O(Nlog N)

# y는 내림차순, x는 오름차순 정렬
points.sort(key=lambda x: x[0])

min_width = float('inf')
left = 0
y_sorted_list = SortedList()

for right in range(n):
    # 2. 현재 점의 y좌표를 SortedList에 추가 (자동 정렬됨)
    y_sorted_list.add(points[right][1])

    # 3. y의 최댓값과 최솟값 차이가 D 이상인 동안 left를 당기며 최소 폭 갱신
    while y_sorted_list[-1] - y_sorted_list[0] >= d:
        width = points[right][0] - points[left][0]
        if width < min_width:
            min_width = width

        # 윈도우를 벗어나는 left 점의 y좌표를 제거
        y_sorted_list.remove(points[left][1])
        left += 1

# 결과 출력
print(min_width if min_width != float('inf') else -1)