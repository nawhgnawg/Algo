# 성냥개비
# https://www.acmicpc.net/problem/3687

# 1차 - 그리디
# 각 숫자별 들어가는 성냥 수
# 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9:6, 0: 6
import sys
input = sys.stdin.readline

dp = [float('inf')] * 101
init_list = ['', '', 1, 7, 4, 2, 6, 8]  # 최소 값
for i in range(2, 8):
    dp[i] = init_list[i]

for i in range(8, 101):
    for j in range(2, i - 1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i - j]) + '0'))

# 가장 큰수는 11..11 or 71..11 밖에 될 수가 없다!
def find_biggest(num):
    result = '1' * (num // 2)
    if num % 2:
        result = '7' + result[1:]
    return result

def find_smallist(num):
    return dp[num]

T = int(input())
for _ in range(T):
    N = int(input())
    print(find_smallist(N), find_biggest(N))