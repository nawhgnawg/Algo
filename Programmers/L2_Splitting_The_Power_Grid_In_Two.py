# 프로그래머스 Level 2 - 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971


# 주어진 전선을 그래프(인접 리스트) 로 표현합니다.
# 전선 하나를 끊는다고 가정하고, BFS 또는 DFS로 한 쪽 전력망의 송전탑 개수를 셉니다.
# 두 전력망의 송전탑 개수 차이를 구하고, 그 중 최솟값을 선택합니다.

from collections import defaultdict
def solution(n, wires):
    def dfs(start, visited, graph):
        stack = [start]
        count = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                count += 1
                stack.extend(graph[node])
        return count

    answer = n  # 최대 차이는 n-1이므로 큰 값으로 초기화

    for cut in wires:
        # 그래프 초기화
        graph = defaultdict(list)
        for a, b in wires:
            if (a, b) == cut or (b, a) == cut:  # 끊는 간선 제외
                continue
            graph[a].append(b)
            graph[b].append(a)

        # 끊은 전선의 한쪽 끝에서 DFS 시작
        visited = set()
        a, b = cut
        count = dfs(a, visited, graph)  # 한쪽 그룹 크기
        diff = abs((n - count) - count)  # 두 전력망 차이
        answer = min(answer, diff)

    return answer

n, wires = 9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]      # return 3
# n, wires = 4, [[1, 2], [2, 3], [3, 4]]      # return 0
# n, wires = 7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]      # return 1
print(solution(n, wires))