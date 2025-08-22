# 2021 KAKAO BLIND RECRUITMENT - 매출 하락 최소화
# https://school.programmers.co.kr/learn/courses/30/lessons/72416

sales = [5, 6, 5, 3, 4]
links = [[2, 3], [1, 4], [2, 5], [1, 2]]
result = 6

from collections import defaultdict     # 트리 연결 방식

def solution(sales, links):
    answer = 0
    # 번호: 급여
    d = {}
    for i in range(len(sales)):
        d[i + 1] = sales[i]

    # 팀장 - 팀원 연결
    tree = defaultdict(list)
    for parent, child in links:
        tree[parent].append(child)

    print(tree)

    return answer

print(solution(sales, links) == result)