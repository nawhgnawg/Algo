# 프로그래머스 Level 2 - 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

# 바로 밑으로 갈 수 없음, 대각 좌, 우 둘 중 하나
# BFS or DFS 문제 X, 그리디 X -> DP(동적 계획법)으로 풀어야함!
# dp[i][j] = land[i][j] + max(dp[i-1][k])   (단, k != j)
def solution(land):
    n = len(land)

    # DP 테이블 (land 자체를 갱신하면서 사용 가능)
    for i in range(1, n):
        for j in range(4):
            max_val = 0
            for k in range(4):  # 위 행의 4개 열을 확인
                if k != j:      # 같은 열은 건너뜀
                    if land[i - 1][k] > max_val:
                        max_val = land[i - 1][k]

            land[i][j] += max_val  # 현재 칸 값에 최적의 위쪽 값 더하기

    return max(land[-1])

# def solution(land):
#     answer = 0
#     n = len(land)
#     pre_i, pre_j = 0, 0
#     for i in range(n):
#         max_num = 0
#         for j in range(4):
#             if land[i][j] > max_num and i != pre_i + 1 and j != pre_j:
#                 max_num = land[i][j]
#                 pre_i, pre_j = i, j
#         answer += max_num
#
#     return answer
# i = 1, j = 0, k = 0 -> 0 != 0
# i = 1, j = 0, k = 1 -> 1 != 0 -> land[0][1] > 0 -> max_val = 2
# i = 1, j = 0, k = 2 -> 2 != 0 -> land[0][2] > 2 -> max_val = 3
# i = 1, j = 0, k = 3 -> 3 != 0 -> land[0][3] > 3 -> max_val = 5 -> land[1][0] = 10
# i = 1, j = 0, k = 3 -> 3 != 0 -> land[0][3] > 3 -> max_val = 5
land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]       # return 16
print(solution(land))