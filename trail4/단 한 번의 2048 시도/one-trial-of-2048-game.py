# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# 해결 방법
# 왼쪽으로 미는 함수를 정의하고, 오른쪽은 슬라이싱을 이용해서 뒤집은 다음 밀고 결과를 뒤집고
# 위, 아래는 세로열을 뽑아와 똑같이 처리하고 다시 새로열에 넣어준다.

def push_left(row):
    # 빈칸을 제외하고 숫자만 순서대로 모은다.
    nums = [x for x in row if x != 0]

    merged = []
    i = 0
    # 인접한 숫자가 같으면 합치고, 아니면 그냥 추가
    while i < len(nums):
        # 현재 숫자가 다음과 같으면 합침
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            merged.append(nums[i] * 2)
            i += 2
        # 다르면 그냥 추가
        else:
            merged.append(nums[i])
            i += 1
    
    # 남은 빈칸만큼 0을 추가
    return merged + [0] * (4 - len(merged))


if dir == 'L':
    for i in range(4):
        grid[i] = push_left(grid[i])

elif dir == 'R':
    for i in range(4):
        # 행을 뒤집어서 넣고 다시 뒤집기
        grid[i] = push_left(grid[i][::-1])[::-1]

elif dir == 'U':
    for j in range(4):
        # j번째 세로열을 뽑아오기
        col = [grid[i][j] for i in range(4)]
        new_col = push_left(col)
        # 처리된 결과를 다시 세로줄에 덮어쓰기
        for i in range(4):
            grid[i][j] = new_col[i]

elif dir == 'D':
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        new_col = push_left(col[::-1])[::-1]
        for i in range(4):
            grid[i][j] = new_col[i]

for row in grid:
    print(*(row))
    

    