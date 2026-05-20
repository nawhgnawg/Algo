m1, d1, m2, d2 = map(int, input().split())

def calc_day(month, day):
    days = 0
    for i in range(1, month):
        # 31일 인날
        if i in [1, 3, 5, 7, 8, 10, 12]:
            days += 31
        elif i == 2:
            days += 28
        else:
            days += 30
    days += day
    return days

before_days = calc_day(m1, d1)
after_days = calc_day(m2, d2) + 1

print(after_days - before_days)
            


