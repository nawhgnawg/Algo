# 프로그래머스 - 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]


# 1차
def time_convert(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m

def solution1(book_time):
    answer = 0
    check_change_list = list()
    for start, end in book_time:
        check_change_list.append((time_convert(start), 1))
        check_change_list.append((time_convert(end) + 10, 0))

    check_change_list.sort()
    print(check_change_list)

    tmp = 0
    for t, chk in check_change_list:
        if chk == 0:
            tmp += -1
        else:
            tmp += 1
        answer = max(answer, tmp)
    return answer

print(solution1(book_time))