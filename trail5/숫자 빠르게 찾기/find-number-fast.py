n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# 1. 각 숫자의 위치(인덱스 + 1)를 미리 딕셔너리에 등록 (딱 한 번만 실행: O(N))
pos_dict = {}
for idx, num in enumerate(arr):
    pos_dict[num] = idx + 1

# 2. 쿼리 수행 (각 쿼리당 O(1)만에 위치 조회)
for q in queries:
    if q in pos_dict:
        print(pos_dict[q])
    else:
        print(-1)