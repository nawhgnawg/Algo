from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

num_count = defaultdict(int)
max_len = 0
left = 0

for right in range(n):
    # 1. right 원소를 윈도우에 추가하고 개수 증가
    num_count[arr[right]] += 1
    
    # 2. 어떤 원소의 개수가 k개를 초과하면, 조건을 만족할 때까지 left를 우측으로 이동
    while num_count[arr[right]] > k:
        num_count[arr[left]] -= 1
        if num_count[arr[left]] == 0:
            del num_count[arr[left]]
        left += 1

    # 3. 현재 유효한 윈도우의 길이 갱신
    current_len = right - left + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)    