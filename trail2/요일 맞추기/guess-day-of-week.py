m1, d1, m2, d2 = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

def calc_day(month, day):
    return sum(days_in_month[:month]) + day

before_day = calc_day(m1, d1)
after_day = calc_day(m2, d2)

day = (after_day - before_day) % 7
print(days[day])

