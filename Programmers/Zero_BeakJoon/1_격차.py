# 1. 격차

# 모든 학생들이 얻은 점수 중에서 가장 큰 점수와 가장 작은 점수의 차이를 반환하여라.
def solution(n, scores):
    return max(scores) - min(scores)

# n, scores = 8, [7, 7, 5, 8, 9, 4, 6, 2]                     # return 7
# n, scores = 10, [5, 3, 7, 5, 3, 3, 6, 1, 8, 7]              # return 7
# n, scores = 12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]     # return 11
n, scores = 2, [5, 5]                                       # return 0
print(solution(n, scores))
