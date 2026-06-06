n = int(input())
numbers = [int(input()) for _ in range(n)]

first_seen = {0: -1}

current_sum = 0
max_length = 0

for i in range(n):
    # 현재까지의 누적합을 구하고 7로 나눈 나머지 연산
    current_sum += numbers[i]
    remainder = current_sum % 7

    # 이 나머지를 이전에 본적이 있다면 -> 7의 배수 구간 발견
    if remainder in first_seen:
        length = i - first_seen[remainder]
        max_length = max(max_length, length)
    else:
        # 처음보는 나머지라면 현재 인덱스를 기록
        first_seen[remainder] = i

print(max_length)

    
