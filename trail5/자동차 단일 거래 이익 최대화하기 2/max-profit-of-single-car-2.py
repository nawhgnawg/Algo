n = int(input())
price = list(map(int, input().split()))

min_price = price[0]
max_profit = 0

for i in range(1, n):
    current_profit = price[i] - min_price

    max_profit = max(max_profit, current_profit)
    min_price = min(price[i], min_price)

print(max_profit)
