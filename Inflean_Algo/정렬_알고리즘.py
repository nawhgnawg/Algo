# title 버블 정렬

# contents 버블 정렬
# 데이터의 인접 요소끼리 비교하고, swap 연산을 수행하며 정렬하는 방식
# 시간 복잡도: O(N²)

# contents 선택 정렬
# 데이터에서 최대나 최소 데이터를 데이터가 나열된 순으로 찾아가며 선택하는 방식
# 시간 복잡도: O(N²)

# contents 삽입 정렬
# 이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치에 삽입시켜 정렬하는 방식
# 시간 복잡도: O(N²)
# 적절한 삽입 위치를 탐색하는 부분에서 이진 탐색(Binary Search)등과 같은 탐색 알고리즘을 사용하면 시간 복잡도를 줄일 수 있다.

# example 백준 11399 - 실버 3 - ATM 인출 시간 계산하기
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# p = list(map(int, input().split()))
#
# p.sort()
# answer = 0
# current_time = 0
# for t in p:
#     current_time += t
#     answer += current_time
#
# print(answer)

# process 삽입 정렬 구현
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
s = [0] * n

for i in range(1, n):
    insert_point = i
    insert_value = p[i]
    for j in range(i - 1, - 1, -1):
        if p[j] < p[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0

    # 한칸씩 Shift
    for j in range(i, insert_point, -1):
        p[j] = p[j - 1]

    # 삽입 위치에 데이터 저장
    p[insert_point] = insert_value

s[0] = p[0]
for i in range(1, n):
    s[i] = s[i - 1] + p[i]

print(sum(s))