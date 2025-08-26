# 프로그래머스 Level 2 - 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A, B):
    answer = 0
    # 한쪽은 값을 오름차순으로 정렬, 다른 한쪽은 값을 내림차순으로 정렬
    sort_a = sorted(A, reverse=False)
    print(sort_a)
    sort_b = sorted(B, reverse=True)
    print(sort_b)
    for i in range(len(A)):
        answer = answer + (sort_a[i] * sort_b[i])

    return answer

print(solution([1, 4, 2], [5, 4, 4]))