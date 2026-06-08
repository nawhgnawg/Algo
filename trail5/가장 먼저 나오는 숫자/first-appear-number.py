from bisect import bisect_left

n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:

    # 1. q가 있어야 할 위치를 이진 탐색으로 즉시 검색
    idx = bisect_left(arr, q)

    # 2. 인덱스가 배열 범위 내에 있고, 실제 그 자리의 값이 q가 맞다면 존재하는 것!
    if idx < n and arr[idx] == q:
        print(idx + 1)
    else:
        print(-1)
    
    # q in arr은 배열의 첫 번째 원소부터 마지막 원소까지
    # 하나하나 다 확인하는 $O(N)$ 연산입니다.
    
    # if q in arr:
    #     print(bisect_left(arr, q) + 1)
    # else:
    #     print(-1)