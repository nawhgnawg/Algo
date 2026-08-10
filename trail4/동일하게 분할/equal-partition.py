n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)

# 1. 전체 합이 홀수라면, 애초에 두 그룹으로 똑같이 나눌 수 없습니다.
if total_sum % 2 != 0:
    print("No")
else:
    target = total_sum // 2

    # dp[i] : 주어진 숫자를 1번씩만 조합해서 합 i를 만들 수 있는지 여부
    dp = [False] * (total_sum + 1)
    dp[0] = True  # 합 0은 아무것도 고르지 않으면 되므로 True

    for num in arr:
        for i in range(target, num - 1, -1):
            # 과거에 i - num을 만드는 것이 가능했다면
            # 거기에 num을 더한 합도 가능하다. 
            if dp[i - num]:
                dp[i] = True

    if dp[target]:
        print("Yes")
    else:
        print("No")

    