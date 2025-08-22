# 프로그래머스 - 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# 1차 - 62.5점
def solution(fees, records):
    answer = []
    end = 24 * 60 - 1
    ft, ff, pt, pf = fees

    a = {}
    fee = []

    for record in records:
        time, number, io = record.split()
        h, m = time.split(":")
        mTime = int(h) * 60 + int(m)  # 분으로 통일
        # 저장할 내용 = IN이면 해당 차량 번호에 들어간 시간 저장, OUT이면 해당 차량 번호의 (지금시간 - 들어간 시간)반환
        if io == "IN":
            a[number] = mTime
        else:
            fee.append([number, mTime - a[number]])
            a.pop(number)
    # IN하고 OUT하지 않은 차들을 계산 못했음
    while len(a) > 0:
        number, mTime = a.popitem()
        print(number, mTime)
        fee.append([number, end - mTime])

    s_fee = sorted(fee)
    f_dict = {}
    for number, mTime in s_fee:
        if number in f_dict:
            f_dict[number] += mTime
        else:
            f_dict[number] = mTime

    # 가격 계산
    for number, mTime in f_dict.items():
        if mTime < ft:
            answer.append(ff)
        else:
            if mTime % pt != 0:
                total = ff + (int((mTime - ft) / pt) + 1) * pf
            else:
                total = ff + int((mTime - ft)/pt) * pf
            answer.append(total)
    return answer



print(solution(fees, records))