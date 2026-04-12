n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

gold_price = 0


def find_gold(r, c, k):
    gold = 0
    for i in range(n):
        for j in range(n):
            if abs(r - i) + abs(c - j) <= k:
                gold += grid[i][j]
    
    return gold


max_gold = 0

# 1. 모든 격자의 위치를 중심점(i, j)으로 설정
for i in range(n):
    for j in range(n):
        # 2. 마름모의 크기를 0부터 격자 전체를 덮을 수 있는 크기 (2 * n)까지 키워봄
        for k in range(2 * n + 1):
            current_gold = find_gold(i, j, k)
            cost = k ** 2 + (k + 1) ** 2
            # 손해를 보지 않는 경우에만 갱신
            if current_gold * m >= cost:
                max_gold = max(max_gold, current_gold)

print(max_gold)

