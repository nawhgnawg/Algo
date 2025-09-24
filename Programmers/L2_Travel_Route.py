# 프로그래머스 Level 3 - 여행 경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164


# 티켓을 출발지 기준으로 정렬 (알파벳 순서대로 경로가 나오도록)
# DFS로 경로를 하나씩 만들어 감.
#   현재 공항에서 갈 수 있는 티켓을 순회.
#   그 티켓을 사용했다고 표시하고 다음 공항으로 이동.
#   모든 티켓을 사용했다면 경로를 반환.
# 가장 먼저 완성되는 경로가 곧 사전순으로 가장 앞선 경로.
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
                    return result

                # 백트래킹
                path.pop()
                used[i] = False
        return None

    return dfs("ICN", 0)

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]      # return ["ICN", "JFK", "HND", "IAD"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]      # return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution(tickets))