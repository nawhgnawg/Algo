n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 1. 첫 장소의 가격을 현재까지의 최저가로 설정
min_cost = cost[0]
total_expense = 0

# 2. 마지막 장소는 도착점일 뿐 에너지를 살 가치가 없음
for i in range(n - 1):
    # 현재 도착한 장소의 가격이 기존 최저가보다 싸다면 최저가 갱신
    if cost[i] < min_cost:
        min_cost = cost[i]

    # 현재까지 발견한 가장 싼 값으로 다음 장소에 갈 거리만큼 에너지를 구매
    total_expense += min_cost * dist[i]

print(total_expense)