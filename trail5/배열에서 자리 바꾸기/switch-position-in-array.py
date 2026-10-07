class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 두 노드를 안전하게 연결하는 함수
def connect(u, v):
    if u is not None:
        u.next = v
    if v is not None:
        v.prev = u


N = int(input())
Q = int(input())

# 1~N 노드 생성 및 오름차순 연결 (1-indexed)
nodes = [None] + [Node(i) for i in range(1, N + 1)]
for i in range(1, N):
    connect(nodes[i], nodes[i + 1])

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    
    A, B = nodes[a], nodes[b]
    C, D = nodes[c], nodes[d]
    
    A_prev, B_next = A.prev, B.next
    C_prev, D_next = C.prev, D.next

    # Case 1: [a, b] 바로 뒤에 [c, d]가 붙어있는 경우
    if B.next == C:
        connect(A_prev, C)
        connect(D, A)
        connect(B, D_next)
    # Case 2: [c, d] 바로 뒤에 [a, b]가 붙어있는 경우
    elif D.next == A:
        connect(C_prev, A)
        connect(B, C)
        connect(D, B_next)
    # Case 3: 두 구간이 떨어져 있는 경우
    else:
        connect(A_prev, C)
        connect(D, B_next)
        connect(C_prev, A)
        connect(B, D_next)

# 시작 노드(Head) 찾기 (prev가 None인 노드)
head = nodes[1]
while head.prev is not None:
    head = head.prev

# 결과 출력
cur = head
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next
print()