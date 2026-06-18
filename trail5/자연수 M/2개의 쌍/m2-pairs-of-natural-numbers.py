N = int(input())
numbers = []

for i in range(N):
    count, x = map(int, input().split())
    numbers.append([x, count])

# 1. 숫자 크기 순으로 오름차순
numbers.sort()

left = 0
right = N - 1
max_pair_sum = 0

# 2. 양 끝에서 투 포인터로 좁혀오면서 매칭
while left <= right:
    # 1. 좌우 포인터가 만났다면, 남은 개수와 상관없이 자기 자신끼리 짝을 지어야 합니다.
    if left == right:
        max_pair_sum = max(max_pair_sum, numbers[left][0] * 2)
        break
        
    # 2. 가장 작은 수와 가장 큰 수의 합 계산 및 최댓값 갱신
    current_sum = numbers[left][0] + numbers[right][0]
    if current_sum > max_pair_sum:
        max_pair_sum = current_sum
    
    # 3. 양 끝 카드의 남은 수량 비교하여 포인터 이동
    if numbers[left][1] < numbers[right][1]:
        # 왼쪽 카드가 더 적다면, 왼쪽 카드를 전부 소모하고 left를 한 칸 전진
        numbers[right][1] -= numbers[left][1]
        left += 1
    elif numbers[left][1] > numbers[right][1]:
        # 오른쪽 카드가 더 적다면, 오른쪽 카드를 전부 소모하고 right를 한 칸 후진
        numbers[left][1] -= numbers[right][1]
        right -= 1
    else:
        # 양쪽 카드의 개수가 완벽히 같다면 둘 다 동시에 소모하고 양쪽 포인터 이동
        left += 1
        right -= 1

print(max_pair_sum)

