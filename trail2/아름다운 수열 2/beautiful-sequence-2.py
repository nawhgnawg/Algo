n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1. B를 미리 정렬해 둡니다.
sorted_b = sorted(b)

answer = 0

# 아름다운 수열 만들기


# 2. A에서 길이가 m인 모든 연속 구간을 탐색합니다. (0부터 n - m까지)
for i in range(n - m + 1):
    # 구간을 잘라내어 정렬한 뒤, sorted_b와 같은지 비교
    if sorted(a[i : i + m]) == sorted_b:
        answer += 1

print(answer)