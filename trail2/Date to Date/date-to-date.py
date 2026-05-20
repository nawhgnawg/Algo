# m1, d1, m2, d2 = map(int, input().split())

# def calc_day(month, day):
#     days = 0
#     for i in range(1, month):
#         # 31일 인날
#         if i in [1, 3, 5, 7, 8, 10, 12]:
#             days += 31
#         elif i == 2:
#             days += 28
#         else:
#             days += 30
#     days += day
#     return days

# before_days = calc_day(m1, d1)
# after_days = calc_day(m2, d2) + 1

# print(after_days - before_days)
            
m1, d1, m2, d2 = map(int, input().split())

# 1. 인덱스를 월(month)과 일치시키기 위해 0번째에 0을 넣고 각 달의 일수를 저장합니다.
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calc_day(month, day):
    # 2. 파이썬의 sum()과 슬라이싱을 이용하면 for문 없이 한 줄로 계산 가능!
    # 예: month가 3이면 days_in_month[0:3] 즉, 1월과 2월의 일수를 합칩니다.
    return sum(days_in_month[:month]) + day

before_days = calc_day(m1, d1)
after_days = calc_day(m2, d2)

# 3. 시작일을 포함하여 세어야 하므로 마지막에 +1을 해줍니다.
print(after_days - before_days + 1)
