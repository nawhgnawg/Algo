# 1. 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 현재 노드의 상태(이전 노드 / 현재 노드 / 다음 노드)를 출력하는 함수
def print_status(cur):
    prev_str = cur.prev.data if cur.prev else "(Null)"
    cur_str = cur.data
    next_str = cur.next.data if cur.next else "(Null)"
    print(f"{prev_str} {cur_str} {next_str}")

S_init = input()
N = int(input())

# 초기 노드 생성 및 현재 노드로 설정
cur = Node(S_init)

for _ in range(N):
    command = input().split()
    cmd_type = int(command[0])

    if cmd_type == 1:
        # 1 S: cur의 왼쪽에 새로운 노드 삽입
        s = command[1]
        new_node = Node(s)

        new_node.prev = cur.prev
        new_node.next = cur

        if new_node.prev:
            new_node.prev.next = new_node
        cur.prev = new_node

    elif cmd_type == 2:
        # 2 S: cur의 오른쪽에 새로운 노드 삽입
        s = command[1]
        new_node = Node(s)
        
        new_node.prev = cur
        new_node.next = cur.next
        
        if new_node.next:
            new_node.next.prev = new_node
        cur.next = new_node

    elif cmd_type == 3:
        # 3: 왼쪽 노드가 존재하면 이동
        if cur.prev:
            cur = cur.prev

    elif cmd_type == 4:
        # 4: 오른쪽 노드가 존재하면 이동
        if cur.next:
            cur = cur.next

    # 명령 수행 후 현재 노드 상태 출력
    print_status(cur)
