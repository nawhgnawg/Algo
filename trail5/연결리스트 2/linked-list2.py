# 1. 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 노드 u를 현재 연결 리스트에서 뽑아내는 함수
def pop(u):
    if u.prev:
        u.prev.next = u.next
    if u.next:
        u.next.prev = u.prev
    u.prev = None
    u.next = None

# target(i)의 왼쪽에 new_node(j) 삽입
def insert_prev(target, new_node):
    pop(new_node)  # 기존 위치에서 먼저 뽑아냄
    new_node.prev = target.prev
    new_node.next = target
    if new_node.prev:
        new_node.prev.next = new_node
    target.prev = new_node

# target(i)의 오른쪽에 new_node(j) 삽입
def insert_next(target, new_node):
    pop(new_node)  # 기존 위치에서 먼저 뽑아냄
    new_node.next = target.next
    new_node.prev = target
    if new_node.next:
        new_node.next.prev = new_node
    target.next = new_node


n = int(input())
q = int(input())

# 1번부터 N번까지 노드 생성 (1-indexed)
nodes = [None] + [Node(i) for i in range(1, n + 1)]

for _ in range(q):
    queries = list(map(int, input().split()))
    cmd = queries[0]

    if cmd == 1:
        i = queries[1]
        pop(nodes[i])

    elif cmd == 2:
        i, j = queries[1], queries[2]
        insert_prev(nodes[i], nodes[j])

    elif cmd == 3:
        i, j = queries[1], queries[2]
        insert_next(nodes[i], nodes[j])

    elif cmd == 4:
        i = queries[1]
        prev_data = nodes[i].prev.data if nodes[i].prev else 0
        next_data = nodes[i].next.data if nodes[i].next else 0
        print(f"{prev_data} {next_data}")

# 모든 쿼리 수행 후 각 노드의 next 노드 번호 출력
for i in range(1, n + 1):
    next_data = nodes[i].next.data if nodes[i].next else 0
    print(next_data, end=" ")
print()