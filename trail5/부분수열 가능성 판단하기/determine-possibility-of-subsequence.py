n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 핵심 아이디어: 전방 매칭(Prefix Match)과 후방 매칭(Suffix Match)

# 1. pref[i]: B의 0부터 i까지의 원소가 A의 어디까지 매칭되는지 (A의 인덱스 저장)
pref = [-1] * m
a_idx = 0
for b_idx in range(m):
    while a_idx < n and A[a_idx] != B[b_idx]:
        a_idx += 1
    if a_idx == n:  # 더 이상 매칭할 수 없는 경우
        pref[b_idx] = float('inf')
    else:
        pref[b_idx] = a_idx
        a_idx += 1  # 다음 A 원소로 이동

# 2. suff[i]: B의 i부터 m-1까지의 원소가 A의 어디서부터 매칭되는지 (A의 인덱스 저장)
suff = [n] * m
a_idx = n - 1
for b_idx in range(m - 1, -1, -1):
    while a_idx >= 0 and A[a_idx] != B[b_idx]:
        a_idx -= 1
    if a_idx < 0:
        suff[b_idx] = -float('inf')
    else:
        suff[b_idx] = a_idx
        a_idx -= 1  # 이전 A 원소로 이동

answer = 0

# 3. 각 i번째 원소를 지웠을 때 성립하는지 O(1)로 확인
for i in range(m):
    # i를 지웠을 때의 좌측 끝점과 우측 시작점 비교
    left_match = pref[i - 1] if i > 0 else -1
    right_match = suff[i + 1] if i < m - 1 else n
    
    # 왼쪽 조각이 끝난 위치가 오른쪽 조각이 시작하는 위치보다 왼쪽에 있으면 성립!
    if left_match < right_match:
        answer += 1

print(answer)


# 지울 B 선택
# B에서 원소를 하나씩 지워가며 모든 경우의 수를 다 해보는 방식(Brute Force)
# O(M * (N + M))
# for i in range(m):
#     new_B = [B[j] for j in range(m) if i != j]