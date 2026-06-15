n = int(input())

answer = -1

for fives in range(n // 5, -1, -1):
    remainder = n - (fives * 5)
    
    # 남은 금액이 2로 딱 나누어떨어진다면 최적의 조합을 찾은 것
    if remainder % 2 == 0:
        twos = remainder // 2
        answer = fives + twos
        break

print(answer)
        

