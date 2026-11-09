n = int(input())
a = list(map(int, input().split()))

# 1. 오름차순 정렬
a.sort()

min_diff = float('inf')
left = 0
right = n - 1

while left < right:
    s = a[left] + a[right]
    diff = abs(s)

    if diff < min_diff:
        min_diff = diff
    
    # 합이 0이면 가장 가까운 값(0)이므로 즉시 종료
    if s == 0:
        break
    elif s < 0:
        left += 1
    elif s > 0:
        right -= 1

print(min_diff)