from itertools import combinations

n = int(input())
num = list(map(int, input().split()))

total_sum = sum(num)

min_diff = float('inf')

for group1 in combinations(num, n):

    # 그룹 1의 합
    sum1 = sum(group1)

    # 그룹 2의 합
    sum2 = total_sum - sum1

    # 두 그룹간의 차이 (절대값)
    diff = abs(sum2 - sum1)

    # 최솟값 갱신
    min_diff = min(diff, min_diff)

print(min_diff)


