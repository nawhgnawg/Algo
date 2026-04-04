n, m = map(int, input().split())

# 1. 2차원 배열 대신 가로줄의 정보를 리스트에 담기
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    # 위에서부터 아래로 사다리를 타야 하므로 정렬하기 편하게 튜플에 담어둔다.(b, a)
    lines.append((b, a))

# b를 기준으로 내림차순 정렬
lines.sort()

# 2. 사다리를 타고 결과를 반환하는 함수
def simulate(selected_lines):
    # 1부터 n까지의 시작 위치 배열
    arr = [i for i in range(1, n + 1)]

    # 선택한 가로줄을 위에서부터 차례로 만나며 스왑
    for b, a in selected_lines:
        # 문제에서 a는 1부터 시작하므로, 배열 인덱스에 맞게 a-1과 a를 스왑합니다.
        arr[a - 1], arr[a] = arr[a], arr[a - 1]
    
    return arr

# 3. 모든 가로줄을 다 썻을 때의 목표 정답 구하기
target_result = simulate(lines)

# 4. 백트래킹 탐색
def dfs(idx, current_selected):
    # 탈출 조건 - M개의 가로줄을 모두 검토했다면
    if idx == m:
        # 현재 고른 가로줄들로 만든 결과가 타겟과 같다면
        if simulate(current_selected) == target_result:
            return len(current_selected)   # 사용한 선분 개수 반환
        else:
            return float('inf') 

    # 경우의 수 1: 현재 가로줄을 선택하는 경우
    current_selected.append(lines[idx])
    val1 = dfs(idx + 1, current_selected)
    current_selected.pop()

    # 경우의 수 2: 현재 가로줄을 선택하지 않는 경우
    val2 = dfs(idx + 1, current_selected)

    # 두 분기 중 더 적은 선분을 사용한 최솟값 반환
    return min(val1, val2)

answer = dfs(0, [])
print(answer)
