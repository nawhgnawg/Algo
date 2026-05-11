n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 양방향 간선 정보 기록
for s, e in edges:
    graph[s].append(e)
    graph[e].append(s)

# 방문한 정점의 수를 세기 위한 변수
visited_count = 0

# dfs 정의
def dfs(vertex):
    global visited_count
    visited[vertex] = True
    visited_count += 1

    # 인접한 노드 중 방문하지 않은 노드들을 재귀적으로 탐색
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)

# 1번 정점에서 시작
dfs(1)
    
print(visited_count - 1)