n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 누적 합 배열 생성
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + arr[i]

# 음수만 있는 경우를 대비해 최댓값 초기화
answer = -float('inf')

# 2. 길이가 k인 모든 구간의 합을 누적 합으로 계산
for i in range(n - k + 1):
    # i부터 i + k - 1까지의 합 = pref[i + k] - pref[i]
    current_sum = pref[i + k] - pref[i]
    if current_sum > answer:
        answer = current_sum

print(answer)

# # 1. 첫 번째 윈도우(0부터 k-1까지)의 합 구하기
# current_sum = sum(arr[:k])
# answer = current_sum

# answer = 0
# for i in range(k, n):
#     # 이전 윈도우의 가장 앞 원소를 빼고, 새로운 원소를 더함
#     current_sum = current_sum - arr[i - k] + arr[i]
#     if current_sum > answer:
#         answer = current_sum

# print(answer)