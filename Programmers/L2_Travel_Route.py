# 프로그래머스 Level 3 - 여행 경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164



def solution(tickets):
    tickets.sort()
    print(f'tickets: {tickets}')
    used = [False] * len(tickets)
    path = ["ICN"]  # 항상 인천에서 출발

    def dfs(curr, cnt):
        print(path)
        if cnt == len(tickets):     # 모든 티켓 사용 완료
            return path[:]

        for i, (start, end) in enumerate(tickets):
            if not used[i] and start == curr:   # 방문하지 않았고, 시작이 현재랑 같을 떄
                used[i] = True
                path.append(end)

                result = dfs(end, cnt + 1)
                if result:
                    print(f"result: {result}")
                    return result

                # 백트래킹
                path.pop()
                used[i] = False
        return None

    return dfs("ICN", 0)

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]      # return ["ICN", "JFK", "HND", "IAD"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]      # return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution(tickets))