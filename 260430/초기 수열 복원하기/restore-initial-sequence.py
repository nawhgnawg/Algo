n = int(input())
adjacent = list(map(int, input().split()))


# 첫번째 숫자를 1부터 N까지 시도
for start_num in range(1, n + 1):
    a = [0] * n
    a[0] = start_num

    used = [False] * (n + 1)
    used[start_num] = True

    is_possible = True

    # 공식에 따라 나머지 숫자들을 순차적으로 결정
    for i in range(1, n):
        next_val = adjacent[i - 1] - a[i - 1]

        # 조건 검사
        # 1. 숫자가 n 안에 있는가
        # 2. 이미 사용된 숫자인가
        if 1 <= next_val <= n and not used[next_val]:
            a[i] = next_val
            used[next_val] = True
        else:
            is_possible = False
            break

    if is_possible:
        print(*(a))
        break

    
    
