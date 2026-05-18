k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ans = 0

# 모든 개발자의 쌍에 대해 완전 탐색
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 자기 자신과의 쌍은 제외
        if a == b:
            continue

        # a가 b보다 모든 경기에서 앞섰는지 확인하는 플레그
        is_always_ahead = True

        # 모든 경기를 돌며 랭킹 확인
        for match in arr:
            # 현재 경기에서 a와 b의 인덱스를 찾음
            rank_a = match.index(a)
            rank_b = match.index(b)

            # 인덱스가 작을수록 높은 순위인데, a의 인덱스가 더 크다면 뒤쳐진것
            if rank_a > rank_b:
               is_always_ahead = False
               break

        if is_always_ahead:
            ans += 1

print(ans) 
