# n: 수열의 길이, m: 우리가 만들어야 할 목표 합
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# dp[i] : 합 i를 만드는 것이 가능한지 여부 (True / False)
dp = [False] * (m + 1)

# 0은 '아무것도 고르지 않는' 방법으로 항상 만들 수 있으므로 True로 시작합니다.
dp[0] = True

# 1. 수열에 있는 숫자를 하나씩 꺼내 봅니다.
for num in arr:
    
    # 2. [가장 중요한 규칙] 한 번씩만 쓸 수 있으므로, 목표 합 m부터 뒤에서부터 훑습니다!
    for i in range(m, num - 1, -1):
        
        # 3. 과거의 합(i - num)을 만드는 것이 가능했다면?
        if dp[i - num]:
            # 거기에 현재 숫자(num)를 더한 합(i)도 가능해집니다!
            dp[i] = True

# 목표 합(m)을 만들 수 있다면 Yes, 불가능하다면 No 출력
if dp[m]:
    print("Yes")
else:
    print("No")