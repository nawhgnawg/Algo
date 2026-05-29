from itertools import permutations

K, N = map(int, input().split())

A = [i + 1 for i in range(K)]

answer = []

def bt():
    if len(answer) == N:
        print(*answer)
        return

    for i in range(1, K + 1):
        # 가지치기 (Pruning) 핵심 로직
        # 바구니에 이미 2개 이상 들어있고 && 맨 마지막 숫자와 그 앞 숫자가 모두 지금 넣을 'i'와 같다면?
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue  # 안 돼! 3번 연속이야! 더 이상 깊게 들어가지 않고 다음 숫자로 패스!
        answer.append(i)
        bt()
        answer.pop()

bt()