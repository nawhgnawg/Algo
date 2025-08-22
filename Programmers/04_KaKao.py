# 2024 KAKAO WINTER INTERNSHIP
# 프로그래머스 - 도넛과 막대 그래프
# https://school.programmers.co.kr/learn/courses/30/lessons/258711

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

# https://velog.io/@seungjae/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2024-KAKAO-WINTER-INTERNSHIP-%EB%8F%84%EB%84%9B%EA%B3%BC-%EB%A7%89%EB%8C%80-%EA%B7%B8%EB%9E%98%ED%94%84-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4Python-%EA%B5%AC%ED%98%84-DFS
# dfs
def solution(edges):
    answer = []

    # 1. 딕셔너리로 그래프 구현하기
    dic = dict()
    max_val = 0
    for edge in edges:
        if max_val < max(edge):
            max_val = max(edge)
        if edge[1] not in dic:
            dic[edge[1]] = []
        if edge[0] not in dic:
            dic[edge[0]] = [edge[1]]
        else:
            dic[edge[0]].append(edge[1])

    # 생성된 정점 찾기
    visited = [0 for i in range(max_val + 1)]
    for i in dic.values():
        for j in i:
            visited[j] = 1
    for i in dic:
        if len(dic[i]) <= 1:
            visited[i] = 1
    for i, val in enumerate(visited):
        if i != 0 and val == 0:
            created_node = i
    result = [0 for i in range(4)]
    visited = [0 for i in range(max_val + 1)]

    # 막대의 특징
    # 마지막에 어디로도 가지 않음
    # 도넛의 특징
    # 순환하여 결국 1로 돌아옴
    # 팔자의 특징
    # 순환하여 결국 1로 돌아옴 2개의 간선이 나가는 노드가 있음
    def dfs(val):
        start = val
        visited[start] = 1
        stack = [val]
        while stack:
            cur = stack.pop()

            if len(dic[cur]) == 0:  # 막대 모양
                result[2] += 1
                return
            if len(dic[cur]) == 1:
                if visited[dic[cur][0]] == 0:
                    stack.append(dic[cur][0])
                else:
                    result[1] += 1
                    return
            if len(dic[cur]) == 2:
                result[3] += 1
                return

    result[0] = created_node
    for i in dic[created_node]:
        dfs(i)

    return result

print(solution(edges))