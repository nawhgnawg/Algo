from collections import deque
N = int(input())


max_val = 1000002 
dist = [-1] * (max_val + 1)

q = deque([N])
dist[N] = 0

# 3. BFS 탐색
while q:
    curr = q.popleft()

    # 1에 도달하면 즉시 출력 (BFS이므로 처음 도달한 것이 최단 거리)
    if curr == 1:
        print(dist[curr])
        break

    # 4가지 연산 시도
    # 각 연산 결과가 범위 내에 있고, 아직 방문하지 않은(-1) 경우에만 이동
    
    # 연산 1: 현재 수에서 1을 뺍니다.
    if curr - 1 >= 1 and dist[curr - 1] == -1:
        dist[curr - 1] = dist[curr] + 1
        q.append(curr - 1)
        
    # 연산 2: 현재 수에 1을 더합니다. (탐색 범위를 n+1 정도로 제한)
    if curr + 1 <= max_val and dist[curr + 1] == -1:
        dist[curr + 1] = dist[curr] + 1
        q.append(curr + 1)
        
    # 연산 3: 2로 나누어 떨어질 경우
    if curr % 2 == 0:
        next_val = curr // 2
        if dist[next_val] == -1:
            dist[next_val] = dist[curr] + 1
            q.append(next_val)
            
    # 연산 4: 3으로 나누어 떨어질 경우
    if curr % 3 == 0:
        next_val = curr // 3
        if dist[next_val] == -1:
            dist[next_val] = dist[curr] + 1
            q.append(next_val)
