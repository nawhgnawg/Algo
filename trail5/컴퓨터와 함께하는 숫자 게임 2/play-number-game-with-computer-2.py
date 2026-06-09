# m = int(input())
# a, b = map(int, input().split())

# arr = [i + 1 for i in range(m)]

# counts = []

# for target in range(a, b + 1):
#     count = 0

#     left = 1
#     right = m

#     while left <= right:
        
#         count += 1

#         mid = (left + right) // 2

#         if mid == target:
#             counts.append(count)
#             break
        
#         if mid > target:
#             right = mid - 1
#         elif mid < target:
#             left = mid + 1
    
# print(min(counts), max(counts))

import sys
# 파이썬의 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m = int(input())
a, b = map(int, input().split())

# 정답을 비교할 최솟값과 최댓값 변수
min_count = float('inf')
max_count = -1

# left, right: 현재 이진 탐색 범위
# count: 현재까지 탐색한 횟수
def find_counts(left, right, count):
    global min_count, max_count
    
    if left > right:
        return
        
    mid = (left + right) // 2
    
    # [핵심] 현재 계산된 mid가 우리가 관심 있는 범위 [A, B] 안에 있다면?
    if a <= mid <= b:
        min_count = min(min_count, count)
        max_count = max(max_count, count)
        
    # 만약 현재 범위가 [A, B]와 전혀 겹치지 않는다면 더 이상 내려갈 필요가 없음 (가지치기)
    # 하지만 겹칠 가능성이 있다면 왼쪽과 오른쪽 자식 노드로 이진 탐색을 계속 이어감
    if left <= right:
        # 왼쪽 절반 탐색 (mid보다 작은 영역)
        if mid >= a: # 탐색 범위가 A보다 클 때만 왼쪽으로 갈 가치가 있음
            find_counts(left, mid - 1, count + 1)
        # 오른쪽 절반 탐색 (mid보다 큰 영역)
        if mid <= b: # 탐색 범위가 B보다 작을 때만 오른쪽으로 갈 가치가 있음
            find_counts(mid + 1, right, count + 1)

# 1부터 M까지의 범위에서 탐색 횟수 1회부터 시작
find_counts(1, m, 1)

print(min_count, max_count)