from collections import Counter

n = int(input())
a = list(map(int, input().split()))

midpoint_counts = Counter()

# 두 수의 합이 짝수이면 그 중점 K = (a_i + a_j) // 2 가 결정된다
# 모든 쌍 (i < j)을 확인하며 가능한 K의 빈도수를 누적
for i in range(n):
    for j in range(i + 1, n):
        total = a[i] + a[j]
        if total % 2 == 0:
            midpoint_counts[total // 2] += 1

print(max(midpoint_counts.values()) if midpoint_counts else 0)


# max_pairs = 0

# for k in range(1, max(a) + 1):
#     pairs = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if a[j] - k == k - a[i]:
#                 pairs += 1

#     max_pairs = max(max_pairs, pairs)

# print(max_pairs)

        
