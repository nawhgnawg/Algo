N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# 각 폭탄이 터졌는지 여부를 저장할 리스트
is_exploded = [False] * N

# 모든 쌍을 비교하여 폭발 조건 확인
for i in range(N):
    for j in range(i + 1, N):        
        # 숫자가 같고 거리가 k 이내인 경우
        if num[i] == num[j] and (j - i) <= K:
            is_exploded[i] = True
            is_exploded[j] = True

# 터진 폭탄들의 번호별 개수 세기
counts = {}
for i in range(N):
    if is_exploded[i]:
        x = num[i]
        counts[x] = counts.get(x, 0) + 1

# 결과 결정
max_exploded_cnt = 0
ans = 0

# 터진 폭탄들을 확인하며 정답 갱신
for n in counts:
    # 더 많이 터진경우 혹은 횟수는 같은데 번호가 더 큰 경우 갱신
    if counts[n] > max_exploded_cnt:
        max_exploded_cnt = counts[n]
        ans = n
    elif counts[n] == max_exploded_cnt:
        if n > ans:
            ans = n

print(ans)

