n = int(input())

left = [0] * 26
right = [0] * 26

# 트리 입력받기
for _ in range(n):
    x, l, r = input().split()
    left[ord(x) - ord("A")] = l
    right[ord(x) - ord("A")] = r

# 전위 순회 (Root -> Left -> Right)
def preorder(node):
    if node == '.':
        return
    idx = ord(node) - ord('A')
    print(node, end='')
    preorder(left[idx])
    preorder(right[idx])

# 3. 중위 순회 (Left -> Root -> Right)
def inorder(node):
    if node == '.':
        return
    idx = ord(node) - ord("A")
    inorder(left[idx])           # 왼쪽 자식으로
    print(node, end="")          # 방문 (출력)
    inorder(right[idx])          # 오른쪽 자식으로

# 4. 후위 순회 (Left -> Right -> Root)
def postorder(node):
    if node == '.':
        return
    idx = ord(node) - ord("A")
    postorder(left[idx])         # 왼쪽 자식으로
    postorder(right[idx])        # 오른쪽 자식으로
    print(node, end="")          # 방문 (출력)

# 항상 'A'가 루트 노드이므로 'A'부터 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()