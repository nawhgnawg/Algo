# 프로그래머스 - 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

# 1차 - dictionary 이용
from collections import defaultdict
def compare(a, b):
    for key, val in a.items():
        if key not in b or val != b[key]:
            return 0
    return 1


def solution(want, number, discount):
    want_dict = {key: val for key, val in zip(want, number)}
    sale_dict = defaultdict(int)

    answer = 0
    length = len(discount)
    for i in range(length):
        sale_dict[discount[i]] += 1
        if i >= 10:
            sale_dict[discount[i - 10]] = max(0, sale_dict[discount[i - 10]] - 1)
        if i >= 9:
            answer += compare(want_dict, sale_dict)

    return answer


# 2차 - list이용
# discount는 14개일 때 5번만 반복하여 확인하면됨 -> range = 5 (14 - 9) len(discount) - 9 -> 0 ~ 9번까지 비교 discount[0:10]
def solution2(want, number, discount):
    answer = 0
    list_all_want = []

    for i in range(len(want)):
        for j in range(number[i]):
            list_all_want.append(want[i])
    list_all_want.sort()

    for i in range(len(discount) - 9):
        list_10 = discount[i: i + 10]
        list_10.sort()
        if list_all_want == list_10:
            answer += 1

    return answer

print(solution2(want, number, discount))