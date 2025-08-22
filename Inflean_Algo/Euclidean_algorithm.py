# 유클리드 호제법

# 최대 공약수
def gcd(num1, num2):
    max_num = max(num1, num2)       # 큰 수
    min_num = min(num1, num2)       # 작은 수
    mod_num = max_num % min_num     # 큰 수 % 작은 수 나머지
    print(f'{max_num} % {min_num} = {mod_num}')
    if min_num % mod_num == 0:
        return mod_num
    else:
        return gcd(min_num, mod_num)

def gcd_pro(a, b):
    if b == 0:                     # b가 0 이면:
        return a                     # a가 최대 공약수
    else:                          # b가 0이 아니면:
        return gcd_pro(b, a % b)     # 재귀 함수

print(gcd(270, 192))
print(gcd_pro(270, 192))

# 최소 공배수 - (num1 * num2) / 최대 공약수
print(270 * 192 // gcd(270, 192))