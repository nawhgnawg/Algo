n = int(input())

nums = []
count = 0

def bt(depth):
    global count

    # 1. 목표 길이 N에 도달한 경우 -> 아름다운수 1개
    if depth == n:
        count += 1
        return
    
    # 2. 목표 길이 N을 초과한 경우 -> 즉시 뒤로 돌아감
    if depth > n:
        return

    # 3. 1, 2, 3, 4 길이의 블록을 각각 하나씩 붙여봄
    for i in range(1, 5):
        bt(depth + i)
    
bt(0)
print(count)