n = int(input())
price = list(map(int, input().split()))

min_price = price[0]
max_profit = 0

for i in range(1, n):
    current_profit = price[i] - min_price

    # 최대 이익 갱신
    if current_profit > max_profit:
        max_profit = current_profit

    # 최솟값 갱신
    if price[i] < min_price:
        min_price = price[i]

print(max_profit)
