# title 스택과 큐
# 리스트에서 조금 더 발전한 형태의 자료구조

# contents 스택
# 스택은 삽입과 삭제 연상이 후입선출(LIFO)로 이루어지는 자료구조
# 스택은 깊이 우선 탐색(DFS), 백트래킹 종류의 코딩 테스트에 효과적이다.
# 삽입 - stack.append()
# 삭제 - stack.pop()
# 스택 탑 조회 - stack[-1]

# contents 큐
# 큐는 삽입과 삭제 연산이 선입선출(FIFO)로 이루어지는 자료구조
# 일반적으로 deque를 이용하여 큐를 구현한다.
# 큐는 너비 우선 탐색(BFS)에서 자주 사용한다.
# 삽입 - queue.append()
# 삭제 - queue.popleft(), queue.pop()
# 조회 - queue[0]

# contents 우선순위 큐
# 우선순위 큐는 값이 들어간 순서와 상관 없이 우선순위가 높은 데이터가 가장 먼저 나오는 자료구조

# example 백준 17298 - 골드 4 - 오큰수
# 탐색문제는 리버스로도 생각해보고, 투 포인터로도 생각해보자.
# 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 된다.
# 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력한다.
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

answer = [0] * n
d = []
# 1. 스택이 채워져 있고 A[index] > A[top] 인 경우 pop한 인덱스를 이용하여 정답 수열에 오큰수를 저장한다. pop은 조건을 만족하는 동안 계속 반복한다.
# 2. 현재 인덱스 스택에 push 하고 다음 인덱스로 넘어간다.
# 3. 과정 1~2를 수열 길이만큼 반복한 다음 현재 스택에 남아 있는 인덱스에 -1을 저장한다.
for i in range(n):
    while d and a[d[-1]] < a[i]:    # 오큰수 조건
        answer[d.pop()] = a[i]      # 정답 리스트에 오큰수 저장
    d.append(i)

while d:
    answer[d.pop()] = -1

result = ""
for i in range(n):
    result += str(answer[i]) + " "

print(result)

# process - 시간 줄인 방법  
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# a = list(map(int, input().split()))
#
# answer = [-1] * n
# stack = []
#
# for i in range(n):
#     while stack and a[stack[-1]] < a[i]:
#         answer[stack.pop()] = a[i]
#     stack.append(i)
#
# print(" ".join(map(str, answer)))

