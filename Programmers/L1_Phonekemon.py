# 프로그래머스 Level 1 - 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중,
# 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

# 이전에 풀었던 코드
# def solution(nums):
#     d = {}
#     for num in nums:
#         d[num] = d.get(num, 0) + 1
#     if len(nums) / 2 > len(d.keys()):
#         return len(d.keys())
#     else:
#         return len(nums) / 2

def solution(nums):
    dic = {}
    total = len(nums) // 2
    for num in nums:
        dic[num] = 0
    if len(dic.keys()) <= total:
        return len(dic.keys())
    else:
        return total

nums = [3, 1, 2, 3]         # return 2
# nums = [3, 3, 3, 2, 2, 4]   # return 3
# nums = [3, 3, 3, 2, 2, 2]   # return 2
print(solution(nums))