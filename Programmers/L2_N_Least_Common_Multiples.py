# 프로그래머스 Level 2 - N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 최대공약수 gcd 활용 → 최소공배수 lcm 구하기
import math
def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = (answer * num) // math.gcd(answer, num)
    return answer

arr = [2, 6, 8, 14]     # return 168
# arr = [1, 2, 3]         # return 6
print(solution(arr))

