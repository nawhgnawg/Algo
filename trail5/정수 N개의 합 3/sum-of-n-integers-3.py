n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 2차원 누적 합 배열 생성 (크기를 (n + 1) x (n + 1)로 설정)
pref = [[0] * (n + 1) for _ in range(n + 1)]

for r in range(n):
    for c in range(n):
        pref[r + 1][c + 1] = arr[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]

answer = 0

for r in range(n - k + 1):
    for c in range(n - k + 1):
        # (r, c)부터 크기 K x K인 정사각형의 우하단 범위는 (r + k, c + k)
        current_sum = (
            pref[r + k][c + k] - pref[r][c + k] - pref[r + k][c] + pref[r][c]
        )
        if current_sum > answer:
            answer = current_sum

print(answer)