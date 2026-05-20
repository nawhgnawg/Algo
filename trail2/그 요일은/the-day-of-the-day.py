m1, d1, m2, d2 = map(int, input().split())
A = input()

days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def calc_day(month, day):
    return sum(days_in_month[:month]) + day

before_day = calc_day(m1, d1)
after_day = calc_day(m2, d2)

# 총 일수(시작일 포함)
total_days = after_day - before_day + 1

# 몇 주가 반복되는지
w = total_days // 7

# 남은 일수
remainder = total_days % 7
target = week.index(A)

# 시작 요일이 월요일이므로 남은 일수보다 인덱스가 적으면 1번 더 등장 
if target < remainder:
    w += 1

print(w)