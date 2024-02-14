# 곱하기 혹은 더하기
S = "02984"     # 각 자리가 숫자로만 이루어진 문자열
result = 0      # 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수

for num in S:
    if result == 0:
        result += int(num)
    else:
        if num == "0" and "1":
            result += int(num)
        else:
            result *= int(num)
'''
for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
'''

print(result)