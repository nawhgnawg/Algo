# 프로그래머스 Level 2 - K 진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def make_k_base(n, k):
    result = ''
    while n > 0:
        result = str(n % k) + result    # 앞에 문자열 값을 더하는 방식으로 구현 가능
        n //= k
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):     # 합성수라면 √num 이하의 약수가 반드시 존재
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_base = make_k_base(n, k)

    # 0으로 구분하여 숫자 덩어리 나누기
    for num in k_base.split('0'):
        if num and is_prime(int(num)):
            answer += 1

    return answer

n, k = 437674, 3         # return 3
# n, k = "110011", "10"        # return 2

print(solution(n, k))