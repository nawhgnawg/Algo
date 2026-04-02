K, N = map(int, input().split())

selected = []
def backtrack(depth):
    # N개의 숫자를 모두 뽑았다면 종료
    if depth == N:
        print(*selected) # 배열 요소를 공백으로 구분하여 출력
        return

    # 1부터 K까지의 숫자를 순서대로 탐색
    for i in range(1, K + 1):
        selected.append(i)
        backtrack(depth + 1)
        selected.pop()

backtrack(0)