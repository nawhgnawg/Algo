# 프로그래머스 Level 2 - 도넛과 막대 그래프
# https://school.programmers.co.kr/learn/courses/30/lessons/258711

from collections import defaultdict

def solution(edges):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set()

    # 1️⃣ 각 노드의 진입/진출 차수 계산
    for a, b in edges:
        out_degree[a] += 1
        in_degree[b] += 1
        nodes.add(a)
        nodes.add(b)
    print(in_degree)
    print(out_degree)
    print(nodes)

    # 2️⃣ 생성점 찾기
    new_node = -1
    for n in nodes:
        if in_degree[n] == 0 and out_degree[n] >= 2:
            new_node = n
            break

    # 3️⃣ 그래프 유형별 개수 계산
    donut = 0
    bar = 0
    eight = 0

    for n in nodes:
        if n == new_node:
            continue
        # 막대 그래프 끝 노드 (out=0)
        if out_degree[n] == 0:
            bar += 1
        # 8자 그래프 중심 노드
        elif in_degree[n] >= 2 and out_degree[n] >= 2:
            eight += 1

    # 도넛은 전체 - 막대 - 8자
    donut = out_degree[new_node] - bar - eight

    return [new_node, donut, bar, eight]


edges = [[2, 3], [4, 3], [1, 1], [2, 1]]        # return [2, 1, 1, 0]
# edges = [[4, 11], [1, 12], [8, 3], [12, 7],
#          [4, 2], [7, 11], [4, 8], [9, 6], [10, 11],
#          [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]        # return [4, 0, 1, 2]
print(solution(edges))