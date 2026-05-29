# 15681번 - 트리와 쿼리
# https://www.acmicpc.net/problem/15681

N = 9  # 트리의 정점의 수
R = 5  # 루트의 번호
Q = 3  # 쿼리의 수
U = [1, 4, 5, 5, 6, 2, 9, 6]  # U[i] -> V[i]
V = [3, 3, 4, 6, 7, 3, 6, 8]
u = [5, 4, 8]


def solution(N, R, Q, U, V, u):
    graph = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        node1, node2 = U[i], V[i]
        graph[node1].append(node2)
        graph[node2].append(node1)

    size = [0] * (N + 1)

    def dfs(curr_node, parent_node):
        size[curr_node] += 1
        for next_node in graph[curr_node]:
            if next_node != parent_node:
                dfs(next_node, curr_node)
                size[curr_node] += size[next_node]

    dfs(R, -1)

    answer = []
    for q in u:
        answer.append(size[q])

    return answer


print(solution(N, R, Q, U, V, u))
