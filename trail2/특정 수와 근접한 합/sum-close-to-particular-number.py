from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_sum = float('inf')

for comb in combinations(arr, n - 2):
    curr_sum = abs(sum(comb) - s)
    min_sum = min(curr_sum, min_sum)

print(min_sum)


