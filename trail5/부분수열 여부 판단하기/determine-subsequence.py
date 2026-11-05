n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0  # 수열 A를 가리키는 포인터
j = 0  # 수열 B를 가리키는 포인터

while i < n and j < m:
    # 값이 일치하면 수열 B의 다음 원소로 포인터 이동
    if A[i] == B[j]:
        j += 1
    
    # 수열 A의 포인터는 항상 전진
    i += 1

# j가 수열 B의 길이와 같다면 모든 원소가 순서대로 매칭된 것
if j == m:
    print("Yes")
else:
    print("No")