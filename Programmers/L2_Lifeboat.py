# 프로그래머스 Level 2 - 구명보트 (그리디)
# https://school.programmers.co.kr/learn/courses/30/lessons/42885


# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# 요약
# 한 번에 최대 2명까지 탈 수 있음
# 무게 합이 limit 이하여야 함
# 필요한 최소 보트 수 구하기

# 그리디, 투 포인터로 해결
def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    answer = 0

    while left <= right:
        # 가장 가벼운 + 가장 무거운 사람이 함께 탈 수 있으면
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            # 아니면 무거운 사람 혼자 태움
            right -= 1
        answer += 1
    return answer

people = [70, 50, 80, 50]       # return 3
limit = 100
# people = [70, 80, 50]           # return 3
# limit = 100
print(solution(people, limit))