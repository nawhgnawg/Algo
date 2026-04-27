N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
max_answer = 0
for i in range(N):
    for j in range(N - 1, 0, -1):
        if arr[j] - arr[i] <= K:
            curr_answer = arr[i: j + 1]
            max_answer = max(len(curr_answer), max_answer)
            break

print(max_answer)