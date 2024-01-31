# 프로그래머스 - 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
name1 = "JEROEN"
name2 = "JAN"


# 1차 - 런타임 에러
def solution1(name):
    # 26개 -> b~m(12) n(1) o~z(12)로 나누기
    answer = 0
    for i in range(len(name)):
        # 문자 값으로 변환
        r = ord(name[i]) - ord('A')
        if r <= 13:
            answer += r
        else:
            r = ord('A') - ord(name[i]) + 26
            answer += r
        # 옆으로 포인터 이동
        answer += 1

    if 'A' in name:
        answer -= name.count('A')

    return answer - 1


# 2차 - 런타임 에러
def solution2(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)

    answer += min_move
    return answer


# 3차
def solution3(name):
    # 두번 꺽는 경우는 고려하지 않음
    if set(name) == {'A'}:
        return 0

    a_pos = ord('A')  # 'A' : 65, 'Z' : 90
    z_pos = ord('Z')

    answer = float('inf')

    for i in range(len(name) // 2 + 1):
        l_r = name[-i:] + name[:-i]  # 왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i::-1] + name[i + 1:][::-1]  # 기준점에서 빠꾸 + 좌측
        for n in [l_r, r_l]:
            # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c) - a_pos, (z_pos + 1) - ord(c)) for c in n]
            answer = min(answer, i + (len(cnt) - 1) + sum(cnt))

    return answer


print(solution3(name2))
