n = int(input())

lr = [tuple(map(int, input().split())) for _ in range(n)]

# 두 선분이 겹치는지 확인하는 함수
def is_overlap(seg1, seg2):
    l1, r1 = seg1
    l2, r2 = seg2
    # 겹친다면 True 반환, 아니면 False반환
    if l1 <= r2 and l2 <= r1:
        return True
    else:
        return False

# 새로 추가할 선분이 기존 선택된 선분들과 겹치지 않는지 확인
def possible(new_seg, current_selected):
    for seg in current_selected:
        if is_overlap(seg, new_seg):
            return False
    return True

def dfs(idx, current_selected):
    # 탈출 - N개의 선분을 모두 검토 완료 했다면 현재까지 모은 개수 반환
    if idx == n:
        return len(current_selected)
    
    max_val = 0

    # 1. 현재 선분을 선택할 수 있는 경우
    if possible(lr[idx], current_selected):
        current_selected.append(lr[idx])
        # 선택했을때의 분기 탐색
        max_val = max(max_val, dfs(idx + 1, current_selected))
        current_selected.pop()

    # 2. 현재(idx 번째) 선분을 선택하지 않고 넘어가는 경우
    max_val = max(max_val, dfs(idx + 1, current_selected))
    
    return max_val

answer = dfs(0, [])
print(answer)