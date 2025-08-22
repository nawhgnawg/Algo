# 프로그래머스 - 여행 경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
dap = ["ICN", "JFK", "HND", "IAD"]

def solution(tickets):
    answer = []
    visited = [False for _ in range(10000)] # 3 ~ 10000개

    start = tickets[0][0]
    end = tickets[0][1]
    data = [start, end]
    cnt = 1
    while cnt < len(tickets):
        new_start = tickets[cnt][0]
        new_end = tickets[cnt][1]
        cnt += 1
        if end == new_start:
            data.append(new_end)
            end = new_end

    return answer

print(solution(tickets).__eq__(dap))