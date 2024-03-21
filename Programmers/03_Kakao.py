# 2023 KAKAO BLIND RECRUITMENT
# 프로그래머스 - 미로 탈출 명령어
# https://school.programmers.co.kr/learn/courses/30/lessons/150365

n, m = 3, 4
x, y = 2, 3     # 출발 위치
r, c = 3, 1     # 종료 위치
k = 5           # 이동 횟수

# 1차 - 경우의 수를 가지치기하고 남은 경우의 수 중 조건을 만족하는 최적해를 찾는 방식 -> 비효율적
def solution1(n, m, x, y, r, c, k):
    answer = ''
    # 방향 우선 순위 : d(아래) -> l(왼쪽) -> r(오른쪽) -> u(위)
    while k:
        # x랑 r을 비교해서 x < r 이면 r-x만큼 d 가기
        if x < r:
            answer += 'd' * (r - x)
            k -= r - x

    return answer

# 2차 - 탐색문제인 척 하는 그리디 문제 + 남은 여유분만큼 우좌 이동을 반복
# 1. 문제의 해를 나누기
# 2. 탈출 불가능 : k가 dist(탈출 최단 거리)보다 작을 경우 + (k - dist)가 홀 수 일 떄

def isVaild(nx, ny, n, m):
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m

def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    None

print(solution1(n, m, x, y, r, c, k))