n = int(input())

# dp[i] = dp[i - 2] + dp[i - 3]
dp = [0] * (n + 1)

dp[0] = 1
if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 1

for i in range(4, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % 10007

print(dp[n])
        