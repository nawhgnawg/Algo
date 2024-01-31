# 큰 수의 법칙

N = 5   # 배열의 크기
M = 8   # 숫자가 더해지는 횟수
K = 3   # 최대 연속에서 더할 수 있는 횟수

array = [2, 4, 5, 4, 6]
result = 0

array.sort()

first = array[-1]
second = array[-2]

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)