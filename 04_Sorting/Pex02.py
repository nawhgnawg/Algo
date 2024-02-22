# 프로그래머스 - H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

citations = [3, 0, 6, 1, 5]

# 1차
def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:    # H_Index 값을 구하기 위해 비교
            return i

    return len(citations)


print(solution(citations))