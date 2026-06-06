n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# 이진탐색 사용
def binary_search(target):
    left = 0
    right = n - 1

    while left <= right:
        # 1. 중간 인덱스 계산
        mid = (left + right) // 2

        # 2. 찾았다면 인덱스 값 반환
        if target == arr[mid]:
            return mid + 1

        # 3. 타겟이 찾는 값보다 작다면 -> right 당김 
        if arr[mid] > target:
            right = mid - 1
        
        # 4. 타겟이 찾는 값보다 크다면 -> left 당김
        if arr[mid] < target:
            left = mid + 1

    # 탐색 범위가 엇갈릴때까지 못찾는다면 -1 반환
    return -1

for q in queries:
    print(binary_search(q))

# 딕셔너리 사용

# # 1. 각 숫자의 위치(인덱스 + 1)를 미리 딕셔너리에 등록 (딱 한 번만 실행: O(N))
# pos_dict = {}
# for idx, num in enumerate(arr):
#     pos_dict[num] = idx + 1

# # 2. 쿼리 수행 (각 쿼리당 O(1)만에 위치 조회)
# for q in queries:
#     if q in pos_dict:
#         print(pos_dict[q])
#     else:
#         print(-1)