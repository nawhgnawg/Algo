# 프로그래머스 Level 2 - 기능 개
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    stack = []
    for p, s in zip(progresses, speeds):
        per = 100 - p
        if per % s == 0:
            date = per // s
        else:
            date = (per // s) + 1
        # date = (per + s - 1) // s  # 올림 처리
        stack.append(date)

    pre = stack[0]
    cnt = 1

    # 앞에서부터 배포 그룹 묶기
    for i in range(1, len(stack)):
        if stack[i] <= pre:
            cnt += 1  # 같은 그룹
        else:
            answer.append(cnt)  # 그룹 완료
            pre = stack[i]  # 새로운 그룹 시작
            cnt = 1

    answer.append(cnt)  # 마지막 그룹 추가

    return answer

progresses, speeds = [93, 30, 55], [1, 30, 5]                           # return [2, 1]
# progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]       # return [1, 3, 2]
print(solution(progresses, speeds))