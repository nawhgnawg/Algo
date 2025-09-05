# 프로그래머스 Level 2 - 삼각 달팽이
# https://school.programmers.co.kr/learn/courses/30/lessons/68645

# n은 1 이상 1,000 이하입니다.

# i = 0 -> j = 1 -> answer[0] = 1
# i = 1 -> j = 2 -> answer[1] = 2
# i = 2 -> j = 3 -> break -> answer[2] = 3
# i = 3 -> j = 4 -> answer[3] = 4 ->

# 1 + 2 + 3 + 4 = 10 = 4 + 5 / 2
# def solution(n):
#     total = int(n * (n + 1) / 2)
#     answer = [i for i in range(1, total + 1)]
#     i = 0
#
#     while i <= total:
#         j = i + 1
#         answer[i] = j
#         if i == 0:
#             i += 1
#
#
#     return answer

# 1. 삼각형 구조 만들기
# 2. 세 방향으로 이동하면서 채우기
# 3. 범위를 벗어나거나 이미 채워져 있으면 방향 전환

def solution(n):
    # 1. 삼각형 구조 초기화
    triangle = [[0] * (i + 1) for i in range(n)]
    total = n * (n + 1) // 2  # 총 채워야 하는 숫자 개수

    # 2. 초기 위치
    row, col = -1, 0
    num = 1

    # 3. 달팽이 채우기
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  # 아래로 이동
                row += 1
            elif i % 3 == 1:  # 오른쪽 이동
                col += 1
            else:  # 왼쪽 위로 이동
                row -= 1
                col -= 1
            triangle[row][col] = num
            num += 1

    # 4. 1차원 배열로 변환
    answer = []
    for row in triangle:
        answer.extend(row)
    return answer
n = 4       # return [1,2,9,3,10,8,4,5,6,7]
# n = 5       # return 	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# n = 6       # return 	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
print(solution(n))
