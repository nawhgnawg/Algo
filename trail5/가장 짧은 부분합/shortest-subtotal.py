n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_len = float('inf')
current_sum = 0
left = 0

# right 포인터를 0부터 n-1까지 이동시킴
for right in range(n):
    current_sum += arr[right]

    # 합이 s 이상인 동안, left를 우측으로 당기며 길이를 줄여봄
    while current_sum >= s:
        # 최소 길이 갱신 (현재 구간의 길이: right - left + 1)
        current_len = right - left + 1
        if current_len < min_len:
            min_len = current_len
        
        # left를 오른쪽으로 한 칸 옮기면서 구간 합에서 제외
        current_sum -= arr[left]
        left += 1

if min_len == float('inf'):
    print(-1)
else:
    print(min_len)