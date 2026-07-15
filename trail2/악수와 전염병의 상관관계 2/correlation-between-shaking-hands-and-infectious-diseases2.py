n, k, p, t = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(t)]

k_count = [0] * n   # 최대 감염 횟수
k_count[p - 1] = k
answer = [0] * n    # 감염 여부
answer[p - 1] = 1

handshakes.sort()

for t, x, y in handshakes:
    # 1. 악수하기 '직전'의 감염 여부를 미리 저장
    is_x_infected = answer[x - 1] == 1
    is_y_infected = answer[y - 1] == 1
    
    # 2. x가 원래 감염자였고 횟수가 남아있을 때
    if is_x_infected and k_count[x - 1] > 0:
        if not is_y_infected:  # y가 정상인이었다면 전염시킴
            answer[y - 1] = 1
            k_count[y - 1] = k

    # 3. y가 원래 감염자였고 횟수가 남아있을 때
    if is_y_infected and k_count[y - 1] > 0:
        if not is_x_infected:  # x가 정상인이었다면 전염시킴
            answer[x - 1] = 1
            k_count[x - 1] = k
    
    # 4. '원래' 감염자였던 사람들의 횟수만 차감합니다.
    # (새로 감염된 사람은 is_x_infected나 is_y_infected가 False이므로 여기서 차감되지 않음)
    if is_x_infected and k_count[x - 1] > 0:
        k_count[x - 1] -= 1
    if is_y_infected and k_count[y - 1] > 0:
        k_count[y - 1] -= 1

for n in answer:
    print(n, end='')