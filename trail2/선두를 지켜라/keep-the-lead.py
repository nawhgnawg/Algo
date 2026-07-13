n, m = map(int, input().split())

pos_a = [0]
pos_b = [0]

# 1. A의 1초 단위 기록 
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_a.append(pos_a[-1] + v)

# 2. B의 1초 단위 위치 기록
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_b.append(pos_b[-1] + v)

# 3. 비디오 판독 (선두 변경 횟수 찾기)
answer = 0
leader = 0 # 1: A가 선두, 2: B가 선두, 0: 아직 아무도 선두가 아님

# 1초부터 끝날 때까지 훑어봄 (A와 B의 총 이동 시간은 동일함)
for i in range(1, len(pos_a)):
    if pos_a[i] > pos_b[i]:
        # 기존 선두가 B(2)였다면 역전이 일어난 것!
        if leader == 2:
            answer += 1
        leader = 1  # 이제부터 선두는 A
    elif pos_a[i] < pos_b[i]:
        # 기존 선두가 A(1)이였다면 역전
        if leader == 1:
            answer += 1
        leader = 2

print(answer)