# 프로그래머스 Level 1 - 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 참가자 중에는 동명이인이 있을 수 있습니다.

# 시간 초과 - O(N2)
# def solution(participant, completion):
#     for comp in completion:
#         if comp in participant:
#             participant.remove(comp)
#     return participant.pop()

# 정렬 후 비교 방식은 O(n log n)
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]  # 마지막 사람이 완주하지 못한 경우

# participant, completion = ["leo", "kiki", "eden"], ["eden", "kiki"]
participant, completion = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
print(solution(participant, completion))