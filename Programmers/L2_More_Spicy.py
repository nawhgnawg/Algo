# 프로그래머스 Level 2 - 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.

# from collections import deque
# def solution(scoville, K):
#     answer = 0
#     sort_scoville = deque()
#     sort_scoville.append(sorted(scoville))
#     while sort_scoville:
#         for i in range(len(sort_scoville)):
#             if sort_scoville[i] < k:
#                 new_scoville = sort_scoville[i] + (sort_scoville[i + 1] * 2)
#                 sort_scoville.popleft()
#                 sort_scoville.popleft()
#                 sort_scoville.append(new_scoville)
#                 sort_scoville = sorted(sort_scoville)
#                 break
#
#     return answer

# 힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다.
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 최소 힙으로 변환
    answer = 0

    while scoville[0] < K:   # 가장 작은 값이 K 이상이 될 때까지
        if len(scoville) < 2:   # 더 이상 섞을 수 없으면 실패
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer

scoville, k = [1, 2, 3, 9, 10, 12], 7       # return 2
print(solution(scoville, k))