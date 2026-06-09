n = int(input())
a = list(map(int, input().split()))

# 1. 초기값 설정: 첫 번째 원소로 시작합니다.
max_sum = a[0]
current_sum = a[0]

# 2. 두 번째 원소부터 끝까지 순회합니다.
for i in range(1, n):
    # '기존에 더해오던 합에 현재 원소를 더한 값'과 '현재 원소 자기 자신' 중 더 큰 것을 선택합니다.
    # 만약 기존 합이 음수였다면 버리고 새로 시작하는 것이 이득이기 때문입니다.
    current_sum = max(a[i], current_sum + a[i])
    
    # 역대 최댓값을 매 순간 갱신합니다.
    max_sum = max(max_sum, current_sum)

print(max_sum)