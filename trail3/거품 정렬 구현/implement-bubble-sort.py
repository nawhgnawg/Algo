n = int(input())
arr = list(map(int, input().split()))


for i in range(n - 1):
    # 이번 턴에 한 번이라도 자리가 바뀐 적이 있는지 기록하는 깃발
    is_sorted = True

    # 맨 끝으로 밀려난 확정된 숫자들을 제외하고 비교 (n - 1 - i)
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # 앞의 숫자가 더 크면 두 숫자의 자리를 바꿈
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_sorted = False   # 자리가 바뀌었으므로 아직 정렬이 덜 되었다고 표시

    # 3. 한 턴을 돌았는데 자리가 단 한 번도 안 바뀌었다면?
    if is_sorted:
        break

print(*arr)
    