n = int(input())
sequence = list(map(int, input().split()))

s = []

for i in range(n):
    s.append((sequence[i], i))

s.sort(key=lambda x: x[0])

# 정렬된 후의 위치를 저장할 배열
ans = [0] * n

# 정렬된 리스트를 돌며 원래 위치에 현재 위치 기록
for i in range(n):
    val, original_idx = s[i]
    ans[original_idx] = i + 1

for x in range(n):
    print(ans[x], end=' ')