N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

max_count = 0

for i in range(N):
    costs = []
    for j in range(N):
        if i == j:
            costs.append(gifts[i][0] // 2 + gifts[i][1])
        else:
            costs.append(gifts[j][0] + gifts[j][1])

    # 싼것부터 사야 최대한 많이 살 수 있으므로 정렬
    costs.sort()

    # 예산 내에서 몇 명까지 줄 수 있는지 계산
    current_sum = 0
    count = 0

    for cost in costs:
        if current_sum + cost <= B:
            current_sum += cost
            count += 1
        else:
            break
    
    # 최대값 갱신
    max_count = max(max_count, count)

print(max_count)