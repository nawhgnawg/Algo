# 프로그래머스 Level 2 - 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

# 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
#    180	       5000        10	       600

def time_convert(t):
    h, m = t.split(':')
    return int(h) * 60 + int(m)

def calc_fee(total_time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees

    if total_time <= basic_time:
        return basic_fee
    else:
        extra_time = total_time - basic_time
        # 단위 시간 올림 처리
        extra_fee = ((extra_time + unit_time - 1) // unit_time) * unit_fee
        return basic_fee + extra_fee

def solution(fees, records):
    answer = []
    dic = {}
    total = {}      # 누적 주차 시간

    for record in records:
        time, car_num, io = record.split()
        time = time_convert(time)
        if io == "IN":      # 처음 들어올 경우
            dic[car_num] = time
        else:
            in_time = dic.pop(car_num)
            total[car_num] = total.get(car_num, 0) + (time - in_time)

    # 출차하지 않은 차량 출차 처리
    for car_num, in_time in dic.items():
        total[car_num] = total.get(car_num, 0) + (time_convert("23:59") - in_time)

    print(total)
    for car_num in sorted(total.keys()):
        fee = calc_fee(total[car_num], fees)
        answer.append(fee)

    return answer


fees = [180, 5000, 10, 600]     # return [14600, 34400, 5000]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]        # return [0, 591]
# records = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
print(solution(fees, records))

