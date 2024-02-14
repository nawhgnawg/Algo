# 거스름 돈
# 시간 복잡도 : O(K)
# - 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받는다.
n = 1260
array = [500, 100, 50, 10]
count = 0

for coin in array:
    count += n // coin
    n %= coin

print(count)