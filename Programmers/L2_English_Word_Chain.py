# 프로그래머스 Level 2 - 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981


# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때,
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

# 각 사람마다 이전에 말한 단어 저장 -> 만약 끝말잇기가 안되거나, 이미 말 했으면 탈락
# def solution(n, words):
#     answer = []
#     people = [[] for _ in range(n)]
#     temp = []
#     count = 0
#     while count != len(words):
#         for i in range(n):  # 0, 1
#             people[i].append(words[count])
#             count += 1
#             if count == len(words):
#                 break
#
#     return answer


# 이전 단어의 마지막 글자 == 현재 단어의 첫 글자인지 확인
# 이전에 등장한 단어가 다시 나오면 탈락
def solution(n, words):
    used = set()   # 이미 나온 단어 저장
    used.add(words[0])  # 첫 단어 추가

    for i in range(1, len(words)):
        prev = words[i-1]
        curr = words[i]

        # 1. 끝말잇기 규칙 위반 (앞 단어 끝 != 현재 단어 시작)
        if prev[-1] != curr[0]:
            return [(i % n) + 1, (i // n) + 1]

        # 2. 이미 말한 단어일 경우
        if curr in used:
            return [(i % n) + 1, (i // n) + 1]

        used.add(curr)

    # 모두 규칙 지켰으면 탈락자 없음
    return [0, 0]

# n, words = 3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]     # return [3, 3]
# n, words = 5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]     # return [0, 0]
n, words = 2, ["hello", "one", "even", "never", "now", "world", "draw"]     # return [1, 3]
print(solution(n, words))