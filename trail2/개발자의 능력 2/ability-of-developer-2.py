from itertools import combinations

ability = list(map(int, input().split()))

total_sum = sum(ability)

min_dist = float('inf')

# for comb1 in combinations(ability, 4):
#     # 6명 중 4명을 뽑고 선택되지 않은 2명의 합: a_sum
#     a_sum = total_sum - sum(comb1)
#     for comb2 in combinations(comb1, 2):
#         b_sum = sum(comb2)
#         c_sum = total_sum - a_sum - b_sum

#         min_sum = min(a_sum, b_sum, c_sum)
#         max_sum = max(a_sum, b_sum, c_sum)
#         dist = max_sum - min_sum
#         min_dist = min(min_dist, dist)

# print(min_dist)

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(6):
            for l in range(k + 1, 6):
                if i == k or i == l or j == k or j == l:
                    continue
                
                sum1 = ability[i] + ability[j]
                sum2 = ability[k] + ability[l]
                sum3 = total_sum - sum1 - sum2

                min_sum = min(sum1, sum2, sum3)
                max_sum = max(sum1, sum2, sum3)
                dist = max_sum - min_sum

                min_dist = min(min_dist, dist)

print(min_dist)
