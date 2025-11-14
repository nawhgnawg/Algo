# 구간 합
# 합 배열을 이용하여 시간 복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘

# 합 배열 만드는 공식: S[i] = S[i - 1] + A[i]
a = [15, 13, 10, 7, 3, 12]
s = [a[0]]
for i in range(1, len(a)):
    num = s[i - 1] + a[i]
    s.append(num)

# print(s)    # [15, 28, 38, 45, 48, 60]

# 구간 합을 구하는 공식(i에서 j까지 구간 합): S[j] - S[i - 1]

# TODO 백준 11660 - 실버 1 - 구간 합 구하기
# return 27, 6, 64
n, m = 4, 3     # 2차원 배열의 크기, 구갑 합 질의의 개수
graph = [[0, 0, 0, 0, 0],
         [0, 1, 2, 3, 4],
         [0, 2, 3, 4, 5],
         [0, 3, 4, 5, 6],
         [0, 4, 5, 6, 7]]
sum_nums = [[2, 2, 3, 4],
            [3, 4, 3, 4],
            [1, 1, 4, 4]]

# process 질의 마다 구하기 -> 시간 초과 O(n^3)
def solution(n, m, graph, sum_nums):
    answer = []
    for i in range(m):
        x1, y1, x2, y2 = sum_nums[i]

        sum = 0
        for j in range(x1 - 1, x2):
            for k in range(y1 - 1,  y2):
                sum += graph[j][k]

        answer.append(sum)

    return answer


# process 구간 합으로 구하기 -> O(n^2)
def solution2(n, m, graph, sum_nums):
    answer = []
    # 전체 구간 합 배열 만들기
    # 합 배열 D[i][j] 초기화 -> D[i][1] = D[i - 1][1] + A[i][1], D[1][j] = D[1][j - 1] + A[1][j]
    # D[i][j]의 값을 채우는 구간 합 공식: D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]
    D = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + graph[i][j]
    print(D)
    # 구간 합 구하기
    # 2,  2,  3,  4 -> D[3][4] - D[1][4] - D[3][1] - D[1][1]
    # X1, Y1, X2, Y2 -> D[X2][Y2] - D[X1- 1][Y2] - D[X2][Y1 - 1] + D[X1 - 1][Y1 - 1]
    for i in range(m):
        x1, y1, x2, y2 = sum_nums[i]
        result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
        answer.append(result)

    return answer



# process 백준 Ver. - 시간 초과
# n, m = map(int, input().split())
# graphs = []
# for _ in range(n):
#     graph = list(map(int, input().split()))
#     graphs.append(graph)
#
# sum_nums = []
# for _ in range(m):
#     nums = list(map(int, input().split()))
#     sum_nums.append(nums)
#
# answer = []
# for i in range(m):
#     x1, y1, x2, y2 = sum_nums[i]
#
#     sum = 0
#     for j in range(x1 - 1, x2):
#         for k in range(y1 - 1,  y2):
#             sum += graphs[j][k]
#
#     print(sum)

# process 백준 Ver.
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# A = [[0] * (n + 1)]
# D = [[0] * (n + 1) for _ in range(n + 1)]
#
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = D[x2][y2] - D[x1- 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
#     print(result)

# print(solution(n, m, graph, sum_nums))
print(solution2(n, m, graph, sum_nums))


# TODO 백준 10986 - 골드 3 - 나머지 합 구하기
# process 구간 합 구했음 -> 메모리 초과
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# # 구간 합들 구하기
# s = [[numbers[i]] * (i + 1) for i in range(len(numbers))]
# print(s)
# for i in range(n):
#     for j in range(i + 1, n):
#         sum = s[i][j - 1] + numbers[j]
#         s[i].append(sum)
# print(s)
#
# count = 0
# for i in range(n):
#     for j in range(i, n):
#         if s[i][j] % m == 0:
#             count += 1
#
# print(count)

# process (A + B) % C 는 ((A % C) + (B % C)) % C 와 같다.
# import sys
# input = sys.stdin.readline
#
# # 1. 리스트 A의 합 배열 S를 생성한다.
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# s = [0] * n     # 합 배열
# c = [0] * m     # 카운트 배열
# answer = 0
#
# s[0] = numbers[0]
# for i in range(1, n):
#     s[i] = s[i - 1] + numbers[i]
#
# # 2. 합 배열 S의 모든 값을 M으로 나머지 연산을 수행해 값을 업데이트 한다. S[i] = S[i - 1] + A[i]
# # 3. 우선 변경된 합 배열에서 원소 값이 0인 개수만 세어 정답에 더하고, 나머지 값이 같은 합 배열의 개수를 센다.
# for i in range(n):
#     remainder = s[i] % m
#     if remainder == 0:
#         answer += 1
#     c[remainder] += 1
#
# for i in range(m):
#     if c[i] > 1:
#         answer += (c[i] * (c[i] - 1) // 2)
#
# print(answer)

# TODO 백준 11003번 - 플래티넘 - 최솟값 찾기 1
# process 시간 초과 - min(a[start: i + 1])는 매번 O(N x L)이 걸림 -> 최악의 경우 5백만 × 5백만 = 25조 연산 → 절대 통과 불가
# import sys
# input = sys.stdin.readline
#
# n, l = map(int, input().split())
# a = list(map(int, input().split()))
#
# d = []
# for i in range(n):
#     start = i - l + 1
#     end = i
#     if start < 0:
#         d.append(min(a[0: i + 1]))
#     else:
#         d.append(min(a[start: i + 1]))
#
# print(d)

# process 슬라이딩 윈도우 + 덱(deque)
import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))

q = deque()     # (값, index)

for i in range(n):
    # 1. 최솟값 가능성이 없는 데이터 삭제 -> 나보다 큰 데이터 삭제하기
    while q and q[-1][0] > a[i]:    # 큐의 제일 끝에 있는 값이 현재 값보다 크다면
        q.pop()

    q.append((a[i], i))     # 큐에 (값, index) 추가
    # 2. window 크기 밖 데이터 삭제
    if q[0][1] <= i - l:    # window 범위를 벗어나면
        q.popleft()

    print(q[0][0], end=' ')