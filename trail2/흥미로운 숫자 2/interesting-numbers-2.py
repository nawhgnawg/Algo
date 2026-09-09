x, y = map(int, input().split())

interesting_numbers = set()

""" 만약 X, Y 값이 1부터라면??"""
# 숫자의 길이 L (1자리 ~ 7자리)
for length in range(1, 8):
    for main_digit in range(10):
        for other_digit in range(10):
            if main_digit == other_digit:
                continue
            
            # other_digit이 들어갈 위치를 하나씩 정해봄
            for pos in range(length):
                digits = [str(main_digit)] * length
                digits[pos] = str(other_digit)

                # 맨 앞자리 수가 0인 수는 유효하지 않음
                if digits[0] == '0':
                    continue
                
                num = int("".join(digits))
                if x <= num <= y:
                    interesting_numbers.add(num)

print(len(interesting_numbers))


# answer = 0

# for num in range(x, y + 1):
#     str_num = str(num)
#     dic = {}
#     for i in range(len(str_num)):
#         if not str_num[i] in dic:
#             dic[str_num[i]] = 1
#         else:
#             dic[str_num[i]] += 1
    
#     if len(dic.keys()) == 2:
#         for v in dic.values():
#             if v == 1:
#                 answer += 1
        
# print(answer)
        
