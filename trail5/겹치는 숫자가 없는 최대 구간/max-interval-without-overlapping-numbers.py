n = int(input())
arr = list(map(int, input().split()))

seen = set()    # 현재 윈도우에 포함된 숫자들을 관리할 집합
max_len = 0
left = 0

for right in range(n):
    # 이미 윈도우 안에 있는 숫자라면, 중복이 사라질 때까지 left를 당김
    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1
    
    # 현재 숫자를 윈도우에 추가
    seen.add(arr[right])

    # 중복없는 가장 긴 구간의 길이
    current_len = right - left + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)

