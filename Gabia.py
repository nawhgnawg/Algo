# 1번 문제 -> 양방향 트리 + DFS

N, u, v, x, y, K, a = 4, [1, 3, 2], [2, 2, 4], [1, 8, 6], [1, 3, 7], 2, [3, 4]

def solution1(N, u, v, x, y, K, a):
    # 양방향 트리
    # 그래프[출발 노드] = (도착노드, 가는비용, 오는비용)
    graph = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        node1, node2 = u[i], v[i]
        cost1, cost2 = x[i], y[i]
        graph[node1].append((node2, cost1, cost2))
        graph[node2].append((node1, cost2, cost1))

    # DFS
    def dfs(curr_node, parent_node):
        has_target = (curr_node in a)  # 서브트리에 타겟 도시가 존재하는가
        subtree_total_cost = 0  # 서브트리를 모두 방문하고 되돌아오는 전체 왕복 시간
        max_save_cost = 0  # 서브트리에서 마지막으로 멈췄을 때 절약할 수 있는 최대 시간

        for next_node, cost_down, cost_up in graph[curr_node]:

            if next_node == parent_node:
                continue

            # 자식 노드 탐색
            child_has_target, child_cost, child_save = dfs(next_node, curr_node)

            # 자식 노드 방향에 방문해야 할 타겟 도시가 있다면
            if child_has_target:
                has_target = True
                # 해당 간선은 무조건 지나야하니까 왕복 비용을 더함
                subtree_total_cost += (child_cost + cost_down + cost_up)
                # 최대 비용 갱신
                if child_save + cost_up > max_save_cost:
                    max_save_cost = child_save + cost_up

        return has_target, subtree_total_cost, max_save_cost

    # 1번에서 DFS 시작
    target_b, total_cost, max_save = dfs(1, -1)

    return total_cost - max_save
print(solution1(N, u, v, x, y, K, a))    # 17

# 2번 축제 부스 문제
# 1단계 - 하루 방문 시 최대 부스 개수
def solution2_1(N, A):
    day_counts = [0] * 101

    for day in A:
        day_counts[day] += 1

    return max(day_counts)

# 2단계 - 하루 방문 시 총 만족도 최댓값
def solution2_2(N, A, X):
    day_counts = [0] * 101

    for i in range(N):
        day = A[i]
        satisfaction = X[i]
        day_counts[day] += satisfaction

    return max(day_counts)

# 3단계 - 부스가 L일부터 R일까지 열릴 때, 하루 최대 부스 개수
def solution2_3(N, L, R):
    day_counts = [0] * 102

    for i in range(N):
        start_day = L[i]
        end_day = R[i]
        for j in range(start_day, end_day + 1):
            day_counts[j] += 1

    return max(day_counts)

    # # Imos법 적용
    # for i in range(N):
    #     start_day = L[i]
    #     end_day = R[i]
    #     day_counts[start_day] += 1
    #     day_counts[end_day + 1] -= 1
    #
    # # 누적합 계산
    # for i in range(1, 101):
    #     day_counts[i] += day_counts[i - 1]

    # answer = max(day_counts[1:101])
    # return answer

# 4단계 - 연속된 M일 방문 시 최대 부스 개수 -> 카운팅 배열 + 슬라이딩 윈도우 (O(N))
def solution2_4(N, M, A):
    day_counts = [0] * 101

    for day in A:
        day_counts[day] += 1

    current_sum = sum(day_counts[1: M + 1])
    max_sum = current_sum

    for i in range(M + 1, 101):
        current_sum = current_sum - day_counts[i - M] + day_counts[i]
        if current_sum > max_sum:
            max_sum = current_sum

    answer = max_sum
    return answer

# 5단계 - 연속된 M일 방문 시 총 만족도 최댓값 -> 카운팅(만족도 매핑) 배열 + 슬라이딩 윈도우 (O(N))
def solution2_5(N, M, A, X):
    day_counts = [0] * 101

    for i in range(N):
        day = A[i]
        satisfaction = X[i]
        day_counts[day] += satisfaction

    current_sum = sum(day_counts[1:M + 1])
    max_sum = current_sum

    for i in range(M + 1, 101):
        current_sum = current_sum - day_counts[i - M] + day_counts[i]
        if current_sum > max_sum:
            max_sum = current_sum

    answer = max_sum
    return answer