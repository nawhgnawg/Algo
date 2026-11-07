# from itertools import combinations

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 투 포인터 -> O(Nlog N) (정렬 시간)

# 1. 오름차순 정렬
arr.sort()

left = 0
right = n - 1
answer = 0

# 2. 양 끝에서 시작하는 투 포인터 탐색
while left < right:
    if arr[left] + arr[right] <= k:
        # left와 right 사이의 모든 조합(right - left 개)이 조건을 만족함
        answer += (right - left)
        left += 1
    else:
        # 합이 k보다 크면 큰 값을 줄여야 하므로 right를 왼쪽으로 이동
        right -= 1

print(answer)

# 모든 조합을 탐색하는 방식 -> O(N^2)
# for comb in combinations(arr, 2):
#     if sum(comb) <= k:
#         answer += 1

# print(answer)