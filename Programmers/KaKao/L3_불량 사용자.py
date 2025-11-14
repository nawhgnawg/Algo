# 프로그래머스 Level 3 - 불량 사용자
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def solution(user_id, banned_id):
    result = set()

    # banned_id 개수만큼 user_id 조합을 만든다
    for users in permutations(user_id, len(banned_id)):
        print(users)
        match = True
        for i in range(len(banned_id)):
            if len(users[i]) != len(banned_id[i]):      # 길이가 안맞을 때
                match = False
                break
            for j in range(len(users[i])):
                if banned_id[i][j] == '*':
                    continue
                if users[i][j] != banned_id[i][j]:
                    match = False
                    break
            if not match:
                break

        # 모든 banned_id 패턴에 매칭된다면, 조합을 set으로 저장
        if match:
            result.add(frozenset(users))

    return len(result)

# user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]                       # return 2
user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]              # return 2
# user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]    # return 3
print(solution(user_id, banned_id))