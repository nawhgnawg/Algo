n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

answer = 0

for c in coins:
    if k == 0:
        break
    answer += k // c
    k %= c

print(answer)