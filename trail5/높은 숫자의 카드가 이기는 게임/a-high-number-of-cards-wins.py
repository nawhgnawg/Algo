from itertools import combinations

N = int(input())
B = [int(input()) for _ in range(N)]

B.sort()

# B가 가진 카드를 빠르게 확인하기 위해 집합(set)을 활용 (in 연산 시간 단축)
b_set = set(B)

# A가 가지고 있는 카드
A = []
for i in range(1, (2 * N) + 1):
    if not i in b_set:
        A.append(i)

# A와 B의 카드를 비교할 포인터 두 개
a_idx = 0
b_idx = 0
point = 0

# 두 포인터가 각각의 카드 뭉치 끝에 도달할 때까지 반복
while a_idx < N and b_idx < N:
    # 만약 A의 카드가 B의 카드보다 크다면 승리!
    if A[a_idx] > B[b_idx]:
        point += 1
        b_idx += 1  # B는 다음 카드를 타겟으로 잡음
        a_idx += 1  # A도 카드를 소모했으므로 다음 카드로
    else:
        # 만약 A의 카드가 B의 카드보다 작거나 같다면, 이 카드를 버려야 합니다.
        # (어차피 이 카드는 현재 B의 카드도 못 이기므로, 더 뒤에 있는 큰 B의 카드는 절대 못 이깁니다.)
        # 따라서 B의 타겟은 그대로 두고, A의 카드만 다음으로 넘겨서 더 큰 숫자를 가져옵니다.
        a_idx += 1

print(point)

