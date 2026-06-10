import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 물건의 정보를 (무게, 가치) 형태로 리스트에 저장
items = []
for _ in range(N):
    weight, value = map(int, input().split())
    items.append((weight, value))

# [핵심] 가성비(가치 / 무게)를 기준으로 '내림차순' 정렬합니다.
# 람다(lambda) 함수를 써서 value / weight 값을 정렬 기준으로 삼습니다.
items.sort(key=lambda x: x[1] / x[0], reverse=True)

total_value = 0.0

for weight, value in items:
    if M == 0:  # 배낭이 가득 찼다면 종료
        break
        
    # Case 1: 물건을 통째로 다 넣을 수 있는 경우
    if weight <= M:
        M -= weight
        total_value += value
    # Case 2: 물건이 너무 무거워서 쪼개서 넣어야 하는 경우
    else:
        # 배낭의 남은 용량(M)만큼만 가성비를 곱해서 가치를 더해줍니다.
        total_value += M * (value / weight)
        M = 0  # 배낭이 가득 참

# 소수점 셋째 자리까지 출력 (문제의 출력 형식을 맞춰줍니다)
print(f"{total_value:.3f}")