# 프로그래머스 - 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870

sequence = [1, 2, 3, 4, 5]
k = 7

# 1차
def solution1(sequence, k):
    strat_index, end_index = 0
    answer = [0, len(sequence)]
    sum = sequence[0]

    # k가 sequence에 있으면 바로 반환 -> 가장 짧음
    if k in sequence:
        answer = [sequence.index(k), sequence.index(k)]
        return answer

    #
    for i in range(len(sequence)):
        sum = sequence[i]
        for j in range(i + 1, len(sequence)):
            sum += sequence[j]
            if sum == k:
                answer = [i, j]
                return answer

    return answer


# 2차
def solution2(sequence, k):
    start = end = 0
    answer = [0, len(sequence)]
    sum = sequence[0]

    while True:
        if sum < k:
            end += 1
            if end == len(sequence):
                break
            sum += sequence[end]
        else:
            if sum == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            sum -= sequence[start]
            start += 1

    return answer

print(solution2(sequence, k))