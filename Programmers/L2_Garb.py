# 프로그래머스 Level 2 - 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# def solution(clothes):
#     answer = 1
#     dic = {i[1]: 0 for i in clothes}
#     for cloth in clothes:
#         dic[cloth[1]] += 1
#     print(dic)
#     if len(dic.keys()) == 1:
#         for count in dic.values():
#             return count
#     for count in dic.values():
#         answer *= count
#     for count in dic.values():
#         answer += count
#     return answer

# ✅ 옷을 입지 않는 경우를 포함 하고 마지막에 모두 안 입는 경우를 1가지를 빼주는게 포인트
def solution(clothes):
    dic = {}
    for cloth, kind in clothes:
        dic[kind] = dic.get(kind, 0) + 1

    answer = 1
    for count in dic.values():
        answer *= (count + 1)  # 옷을 입지 않는 경우도 포함

    return answer - 1  # 모두 안 입는 경우 제외

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]    # return 5
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]                # return 3
print(solution(clothes))