n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = float('inf')

for i in range(n - t + 1):
    cost = 0
    for j in range(t):
        cost += abs(h - arr[i + j])
    
    min_cost = min(min_cost, cost)

print(min_cost)



