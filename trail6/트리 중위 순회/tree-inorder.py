K = int(input())
inorder_traversal = list(map(int, input().split()))

root_idx = ((2 ** K - 1) // 2) + 1

# 각 깊이(레벨)별 노드들을 담을 2차원 리스트 생성
# 깊이가 K이면 레벨은 0부터 K-1까지 존재합니다.
tree_levels = [[] for _ in range(K)]

# 2. 재귀적으로 트리 구조 복원하기
def find_root(left, right, depth):
    # 역전되면 재귀 종료
    if left > right:
        return
    
    # 현재 서브트리의 가운데 인덱스가 '루트'가 됩니다.
    mid = (left + right) // 2
    
    # 해당 깊이(레벨) 리스트에 루트 노드 값 추가
    tree_levels[depth].append(inorder_traversal[mid])
    
    # 왼쪽 자식 트리 탐색 (깊이 + 1)
    find_root(left, mid - 1, depth + 1)
    # 오른쪽 자식 트리 탐색 (깊이 + 1)
    find_root(mid + 1, right, depth + 1)

find_root(0, len(inorder_traversal) - 1, 0)

for level in tree_levels:
    print(*(level))