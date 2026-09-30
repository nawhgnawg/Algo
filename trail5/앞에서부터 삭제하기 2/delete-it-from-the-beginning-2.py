n = int(input())
arr = list(map(int, input().split()))

# 뒤에서부터 원소를 하나씩 추가하며 누적합과 최솟값을 유지
# 초기값: 가장 마지막 원소 (index n-1)
total_sum = arr[-1]
min_val = arr[-1]

max_avg = 0.0

# K는 앞에서 지우는 개수 (1 <= K <= N - 2)
# 남는 구간의 시작 인덱스 i = K (n-2부터 1까지 역순 진행)
for i in range(n - 2, 0, -1):
    total_sum += arr[i]
    min_val = min(min_val, arr[i])
    
    # 최솟값 1개를 제외한 남은 원소 개수 = (n - i - 1)
    cnt = n - i - 1
    current_avg = (total_sum - min_val) / cnt
    
    if current_avg > max_avg:
        max_avg = current_avg

# 소수점 둘째 자리까지 출력
print(f"{max_avg:.2f}")