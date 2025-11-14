# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조


# mats = [5, 3, 2]
# park = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
#         ["A", "A", "-1", "B", "B", "B", "B", "-1"],
#         ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
#         ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
#         ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
#         ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]
# def solution(mats, park):
#     mats = sorted(mats, reverse = True)
#     M, N = len(park), len(park[0])
#
#     k = 0
#     for l in mats:
#         startIdxSet = set((i, j) for i in range(M-l+1) for j in range(N-l+1))
#         print(f"{k} : {startIdxSet}")
#         k = k + 1
#         # for a, b in startIdxSet:
#         #     ret = set()
#         #     for i in range(a,a+l):
#         #         for j in range(b,b+l):
#         #             ret.add(park[i][j])
#         #     if ret == {'-1'}:
#         #         return l
#     return -1
#
# print(solution(mats, park))


# def solution(a, b, c, d):
#     data = [a, b, c, d]
#     data.sort()
#     if data[0] == data[3]:
#         return 1111 * data[0]
#     elif data[0] == data[2]:
#         return (10 * data[0] + data[3]) ** 2
#     elif data[1] == data[3]:
#         return (10 * data[1] + data[0]) ** 2
#     elif data[0] == data[1] and data[2] == data[3]:
#         return (data[0] + data[2]) * abs(data[0] - data[2])
#     elif data[0] == data[1]:
#         return data[2] * data[3]
#     elif data[1] == data[2]:
#         return data[0] * data[3]
#     elif data[2] == data[3]:
#         return data[0] * data[1]
#     else:
#         return min(data)
#     return -1
#
#
# print(solution(4, 1, 4, 4))
#
# num = [4, 1, 4, 4]
# li = [num.count(i) for i in num]
# print("li: ", li)
# print("li.index(): ", li.index(3))
#
# print(not (set("0555") - set(['0', '5'])))
#
#
# def pro(arr, cnt):
#     for i, num in enumerate(arr):
#         if num >= 50 and num % 2 == 0:
#             arr[i] = num // 2
#         elif num < 50 and num % 2 == 1:
#             arr[i] = num * 2 + 1
#     return arr, cnt
#
#
# import re
#
#
# def solution1(myStr):
#     answer = []
#     sp = re.split(r'[a,b,c]', myStr)
#     for s in sp:
#         if s != '':
#             answer.append(s)
#     return answer
#
#
# print(solution1("baconlettucetomato"))
#
# print([[0 for _ in range(4)] for _ in range(4)])
# print([[0] * 4 for _ in range(4)])


# 순열, 조합
import math
from itertools import permutations
from itertools import combinations

nums = [1, 2, 3, 4, 5]
per_count = 0
for i, num in enumerate(permutations(nums, 3)):
    if i == 0:
        print('permutation')

    per_count += 1
    print(num, per_count)

com_count = 0
for i, num in enumerate(combinations(nums, 3)):
    if i == 0:
        print('combinations')

    com_count += 1
    print(num, com_count)

print(f'per_count = {math.perm(5, 3)}')
print(f'comb_count = {math.comb(5, 3)}')