n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

pieces = [1] * k
max_score = 0

def bt(turn):
    global max_score

    # 1. 현재 상태에서 점수 계산
    current_socre = 0
    for p in pieces:
        if p >= m:
            current_socre += 1

    # 최댓값 갱신
    max_score = max(current_socre, max_score)

    # 가지치기 1: 모든 말이 다 도착했다면 더 이상 볼 필요 없이 탐색 종료
    if max_score == k:
        return
    
    # 2. 주어진 턴을 모두 소진했다면 종료
    if turn == n:
        return
    
    # 3. 이번턴의 이동 거리를 k개의 말 중 누구에게 줄지 결정
    for i in range(k):
        if pieces[i] >= m:
            continue

        # 말을 앞으로 전진
        pieces[i] += nums[turn]

        # 다음 턴으로 넘어감
        bt(turn + 1)

        # 원상 복구
        pieces[i] -= nums[turn]

bt(0)

print(max_score)
