# 3. 자신감 점수

def confident_count(arr):
    m = len(arr)
    count = 0
    for i in range(m):
        left = (i - 1) % m
        right = (i + 1) % m
        if arr[i] > arr[left] and arr[i] > arr[right]:
            count += 1
    return count

def solution(n, warriors):
    answer = 0
    for i in range(n):
        temp = warriors[:i] + warriors[i + 1:]  # i번째 전사 제외
        answer = max(answer, confident_count(temp))

    return answer

n, warriors = 8, [7, 7, 5, 8, 9, 4, 6, 2]                       # return 3
# n, warriors = 10, [5, 3, 7, 5, 3, 3, 6, 1, 8, 7]                # return 3
# n, warriors = 12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]       # return 1
print(solution(n, warriors))