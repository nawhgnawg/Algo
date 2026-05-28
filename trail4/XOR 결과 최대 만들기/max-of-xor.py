# 순열
# from itertools import combinations

# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# max_xor = 0

# for com in combinations(A, m):
#     curr_xor = 0
#     for num in com:
#         curr_xor ^= num
#     max_xor = max(curr_xor, max_xor)

# print(max_xor)


# 백트래킹
n, m = map(int, input().split())
A = list(map(int, input().split()))

answer = []

max_xor = 0

def bt(start):
    global max_xor

    if len(answer) == m:
        # XOR 계산
        curr_xor = 0
        for num in answer:
            curr_xor = curr_xor ^ num
        max_xor = max(curr_xor, max_xor)
        return

    for i in range(start, n):
        answer.append(A[i])
        bt(i + 1)
        answer.pop()

bt(0)

print(max_xor)

