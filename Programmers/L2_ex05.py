# 프로그래머스 - 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

storey = 2554
# 1차
def solution1(storey):
    answer = 0
    n = len(str(storey))
    # 6, 7, 8, 9 층
    if storey % 10 > 5:
        answer += 10 - (storey % 10)
        storey += 10 - (storey % 10)
    # 0, 1, 2, 3, 4, 5 층
    elif storey % 10 <= 5:
        answer += storey % 10
        storey -= storey % 10
    a = [0 for _ in range(9)]
    i = 0
    while storey:
        count = 10 ** (n - 1)
        a[i] = storey // count
        storey %= count
        n -= 1
        i += 1
    answer += sum(a)

    return answer

# 2차
# 일의 자리 뿐만 아니라 다른 자릿수도 똑같이 [12345], [6789]로 나눌 수 있다.
def solution2(storey):
    answer = 0
    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10 - remainder
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        else:
            if (storey // 10) % 10 > 4:
                storey += 10 - remainder
            answer += remainder
        storey //= 10

    return answer

print(solution2(storey))
