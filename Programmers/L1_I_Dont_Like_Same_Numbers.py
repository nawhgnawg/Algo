# 프로그래머스 Level 1 - 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    pre = -1
    for i in range(len(arr)):
        if arr[i] != pre:
            pre = arr[i]
            answer.append(arr[i])

    return answer


arr = [1, 1, 3, 3, 0, 1, 1]     # return [1, 3, 0, 1]
print(solution(arr))
