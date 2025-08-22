# 프로그래머스 - 시소 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/152996

weights = [100, 180, 360, 100, 270]

from collections import defaultdict
def solution(weights):
    answer = 0
    weight_dict = defaultdict(int)

    for weight in weights:
        weight_dict[weight] += 1
    print(weight_dict)
    for key, val in weight_dict.items():
        if val > 1:
            answer += val * (val - 1) // 2  # nC2
        if key * 2 in weight_dict:
            answer += val * weight_dict[key * 2]
        if key * 3 % 2 == 0 and key * 3 // 2 in weight_dict:
            answer += val * weight_dict[key * 3 // 2]
        if key * 4 % 3 == 0 and key * 4 // 3 in weight_dict:
            answer += val * weight_dict[key * 4 // 3]
        print(key, val)
    return answer


print(solution(weights))