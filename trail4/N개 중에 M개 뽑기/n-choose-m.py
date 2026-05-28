# 모듈 사용
# from itertools import combinations

# N, M = map(int, input().split())

# arr = [i + 1 for i in range(N)]

# for com in combinations(arr, M):
#     print(*com)


# 백트래킹
n, m = map(int, input().split())

answer = []

def bt(start):
    # [종료 조건] 바구니에 M개의 숫자가 다 담겼다면 출력하고 돌아감
    if len(answer) == m:
        print(*answer)
        return
    
    # start부터 n까지의 숫자를 순회
    for i in range(start, n + 1):
        answer.append(i)        # 1. 숫자를 바구니에 넣음
        bt(i + 1)               # 2. 오름차순을 위해 지금 넣은 숫자(i)보다 큰 것부터 다시 탐색 시작
        answer.pop()            # 3. 위 탐색이 다 끝나고 돌아오면, 방금 넣었던 숫자를 빼서 원래 상태로 복구 (백트래킹!)


bt(1)