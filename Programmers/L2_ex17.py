# 프로그래머스 - 숫자 카드 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/135807

arrayA = [10, 17]
arrayB = [5, 20]

# 1차 - 최대공약수
def solution1(arrayA, arrayB):
    answer = 0
    a, b = arrayA
    return answer

# 2차
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def notDiv(array, gcd):
    for n in array:
        if n % gcd == 0:
            return False
    return True

def solution2(arrayA, arrayB):
    answer = 0

    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for n in arrayA[1:]:
        gcdA = gcd(n, gcdA)

    for n in arrayB[1:]:
        gcdB = gcd(n, gcdB)

    # 첫 번째 조건 - 나누어 떨어지지않는다면
    if notDiv(arrayA, gcdB):
        answer = max(answer, gcdB)

    # 두 번째 조건
    if notDiv(arrayB, gcdA):
        answer = max(answer, gcdA)

    return answer

print(solution2(arrayA, arrayB))