import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 각 숫자(1 ~ M)의 첫 등장 위치(first)와 마지막 등장 위치(last) 기록
first = {i: -1 for i in range(1, m + 1)}
last = {i: -1 for i in range(1, m + 1)}

for i in range(n):
    x = arr[i]
    if 1 <= x <= m:
        if first[x] == -1:
            first[x] = i
        last[x] = i

# 만약 1부터 M 중 아예 등장하지 않는 숫자가 있다면 조건을 만족할 수 없음
for i in range(1, m + 1):
    if first[i] == -1:
        print(-1)
        sys.exit(0)

# 2. 각 L에 대해, 1~M을 모두 포함하기 위해 필요한 최소 R (min_R[L]) 구하기
# 슬라이딩 윈도우 방식으로 O(N)에 계산
min_R = [0] * n
count = [0] * (m + 1)
unique_count = 0
r = 0

for l in range(n):
    while r < n and unique_count < m:
        x = arr[r]
        if 1 <= x <= m:
            if count[x] == 0:
                unique_count += 1
            count[x] += 1
        r += 1

    if unique_count == m:
        min_R[l] = r - 1  # 0-indexed이므로 r - 1
    else:
        min_R[l] = float('inf')  # 더 이상 모든 숫자를 채울 수 없는 경우

    # l을 오른쪽으로 한 칸 옮기기 위해 현재 l의 원소 제거 준비
    x = arr[l]
    if 1 <= x <= m:
        count[x] -= 1
        if count[x] == 0:
            unique_count -= 1

# 3. 각 L에 대해 바깥쪽 조건을 만족하는 최대 허용 R (max_allowed_R[L]) 구하기
# L을 오른쪽에서 왼쪽으로(N-1부터 0까지) 역순으로 훑으며 min(last[x]) 유지
max_allowed_R = [float('inf')] * n
current_min_last = float('inf')

# 숫자들이 첫 등장하는 위치별로 그룹화
first_to_nums = [[] for _ in range(n)]
for x in range(1, m + 1):
    first_to_nums[first[x]].append(last[x])

for l in range(n - 1, -1, -1):
    for l_last in first_to_nums[l]:
        if l_last < current_min_last:
            current_min_last = l_last
    max_allowed_R[l] = current_min_last - 1

# 4. 모든 L에 대해 min_R[L] <= max_allowed_R[L] 조건을 만족하는 최소 길이 찾기
min_len = float('inf')

for l in range(n):
    r = min_R[l]
    if r != float('inf') and r <= max_allowed_R[l]:
        length = r - l + 1
        if length < min_len:
            min_len = length

print(min_len if min_len != float('inf') else -1)