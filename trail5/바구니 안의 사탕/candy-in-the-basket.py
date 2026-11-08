n, k = map(int, input().split())
baskets = []

for _ in range(n):
    candy, pos = map(int, input().split())
    baskets.append((pos, candy))

# 1. 좌표 기준 오름차순 정렬
baskets.sort(key=lambda x: x[0])

max_candies = 0
current_candies = 0
left = 0

# 2. 슬라이딩 윈도우 탐색
for right in range(n):
    current_candies += baskets[right][1]

    # 구간의 크기(좌표 차이)가 2K를 초과하면 left 포인터를 이동시킴
    while baskets[right][0] - baskets[left][0] > 2 * k:
        current_candies -= baskets[left][1]
        left += 1

    # 최댓값 갱신
    if current_candies > max_candies:
        max_candies = current_candies

print(max_candies)
