N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()

max_count = 0

# 2. i번째 학생의 선물을 반값 할인해주는 모든 경우를 시도 (브루트포스)
for i in range(N):
    current_sum = 0
    count = 0
    for j in range(N):
        if i == j:
            price = P[j] // 2
        else:
            price = P[j]
        
        # 예산을 초과하는지 검사
        if current_sum + price <= B:
            current_sum += price
            count += 1
        else:
            break
    
    max_count = max(max_count, count)

print(max_count)
    
        
        



