from collections import Counter

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

answer = 0

# 1. A와 B의 모든 쌍의 합(A[i] + B[j]) 빈도수 집계: O(N^2)
sum_ab = Counter(x + y for x in A for y in B)

# 2. C와 D의 모든 쌍에 대해 -(c + d)가 sum_ab에 존재하는지 확인: O(N^2)
for x in C:
    for y in D:
        target = -(x + y)
        if target in sum_ab:
            answer += sum_ab[target]

print(answer)
