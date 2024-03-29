# 프로그래머스 - 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

numbers = [4, 1, 2, 1]
target = 4


# 1차 - BFS 방식
def solution1(numbers, target):
    answer = 0
    leaves = [0]
    for number in numbers:
        temp = []
        # 자손 노드
        for leaf in leaves:
            temp.append(leaf + number)  # 더하는 경우
            temp.append(leaf - number)  # 빼는 경우
        leaves = temp

    # 모든 경우의 수 계산 후 target과 같은지 확인
    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer


# 2차 - DFS (주로 재귀함수로 구현)
def dfs(numbers, target, idx, values):  # idx: 깊이, values: 더하고 뺄 특정 leaf값
    global cnt

    # 깊이가 끝까지 닿으면
    if idx == len(numbers) and values == target:
        cnt += 1
        return

    # 끝까지 탐색했는데 sum이 target과 다른 값이면 그냥 넘어간다.
    elif idx == len(numbers):
        return

    # 재귀함수로 구현
    dfs(numbers, target, idx + 1, values + numbers[idx])  # 새로운 value 값 세팅
    dfs(numbers, target, idx + 1, values - numbers[idx])


def solution2(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)

    return cnt


def bestSolution(numbers, target):
    if not numbers and target == 0:     # numbers에 값이 있고 target이 0이면 1을 반환
        return 1
    elif not numbers:
        return 0
    else:
        return bestSolution(numbers[1:], target - numbers[0]) + bestSolution(numbers[1:], target + numbers[0])


print(solution2(numbers, target))
