n, k, b = map(int, input().split())

# 1부터 N까지의 숫자 존재 여부를 체크할 배열 (1: 빠진 숫자, 0: 있는 숫자)
is_missing = [0] * (n + 1)
for _ in range(b):
    num = int(input().strip())
    is_missing[num] = 1

# 1. 누적 합(Prefix Sum) 배열 생성 (크기 n + 1)
# pref[x]는 1부터 x까지의 빠진 숫자 총 개수를 의미
pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + is_missing[i]

min_missing = float('inf')

# 2. 모든 길이가 K인 구간 탐색 (시작 인덱스 i는 1부터 n - k + 1까지)
for i in range(1, n - k + 2):
    # i부터 i + k - 1까지의 구간 합 = pref[i + k - 1] - pref[i - 1]
    current_missing = pref[i + k - 1] - pref[i - 1]
    if current_missing < min_missing:
        min_missing = current_missing

print(min_missing)
