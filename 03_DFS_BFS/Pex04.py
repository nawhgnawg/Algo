# 프로그래머스 - 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 💡최소 단계 찾기 -> BFS
#   1) words에 target이 없으면 바로 0을 반환한다.
#   2) 시작 단어부터 시작해서 queue에 담는다. 단계는 0으로 초기화
#   3) 해당 단어가 words에 존재하는 단어들 중 1개의 알파벳값만 다르다면 큐에 넣어주고 반복한다.
#   4) 만약 target값을 찾으면 지금까지 세어준 단계를 반환한다.

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# 1차 - DFS
def solution1(begin, target, words):
    answer = 0
    visited = [False] * len(words)

    return answer

# 2차 - BFS
from collections import deque
def solution2(begin, target, words):
    if target not in words:
        return 0

    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque()
    # 시작 단어와 함께 단계 0으로 초기화
    queue.append([begin, 0])

    while queue:
        now, step = queue.popleft()
        if now == target:
            return step

        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)):   # 단어의 길이만큼 반복하여
                if now[i] != word[i]:   # 알파벳 한개씩 체크하기
                    count += 1
            if count == 1:
                queue.append([word, step + 1])
        print('now :' + now + " " + str(queue))


print(solution2(begin, target, words))