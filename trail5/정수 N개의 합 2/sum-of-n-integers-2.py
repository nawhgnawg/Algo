n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 첫 번째 윈도우(0부터 k-1까지)의 합 구하기
current_sum = sum(arr[:k])
answer = current_sum

answer = 0
for i in range(k, n):
    # 이전 윈도우의 가장 앞 원소를 빼고, 새로운 원소를 더함
    current_sum = current_sum - arr[i - k] + arr[i]
    if current_sum > answer:
        answer = current_sum

print(answer)