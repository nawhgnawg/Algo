# 만들 수 없는 금액
N = 5   # 가지고 있는 동전 개수
array = [3, 2, 1, 1, 9]

array.sort()

target = 1
for x in array:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)
