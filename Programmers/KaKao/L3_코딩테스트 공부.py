# 프로그래머스 Level 3 - 코딩 테스트 공부
# https://school.programmers.co.kr/learn/courses/30/lessons/118668

# 모든 문제를 풀 수 있을 때까지의 최소 시간을 구하는 DP 문제
def solution(alp, cop, problems):
    max_alp = max(p[0] for p in problems)   # 필요한 알고력의 최대값
    max_cop = max(p[1] for p in problems)   # 필요한 코딩력의 최대값
    print(f'max_alp: {max_alp}, max_cop: {max_cop}')

    # 시작값
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    print(f'alp: {alp}, cop: {cop}')

    INF = int(1e9)
    dp = [[INF] * (max_cop + 2) for _ in range(max_alp + 2)]
    dp[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 공부로 능력 올리기
            if a + 1 <= max_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            if c + 1 <= max_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    next_alp = min(max_alp, a + alp_rwd)
                    next_cop = min(max_cop, c + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[a][c] + cost)

    return dp[max_alp][max_cop]


# [문제를 푸는데 필요한 알고력, 문제를 푸는데 필요한 코딩력, 문제를 풀었을 때 증가하는 알고력, 문제를 풀었을 때 증가하는 코딩력, 문제를 푸는데 드는 시간]
alp, cop, problems = 10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]                                # return 15
# alp, cop, problems = 0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]  # return 13
print(solution(alp, cop, problems))