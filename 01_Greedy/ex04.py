# 1이 될 때까지
N = 25  # 어떠한 수
K = 2   # N을 나누는 수
result = 0  # N을 1로 만드는 최소 횟수

while True:
    if N % K == 0:
        result += 1
        N //= K
    else:
        N -= 1
        result += 1

    if N == 1:
        break

print(result)


