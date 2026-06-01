n = int(input())
num = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

jumps = 0
current_jump_end = 0  # 현재 점프 횟수로 갈 수 있는 최대 위치
farthest = 0          # 지금까지 확인한 곳 중 가장 멀리 갈 수 있는 위치

for i in range(n - 1):
    # 1. 현재 위치에서 제일 멀리 뛸 수 있는곳을 갱신
    farthest = max(farthest, i + num[i])

    # 2. 현재 점프로 도달할 수 있는 끝(current_jump_end)에 도달했다면
    if i == current_jump_end:
        jumps += 1               # 점프 횟수 1 증가
        current_jump_end = farthest # 다음 점프의 한계점을 갱신
        
        # 제자리걸음(더 이상 앞으로 못 감)이면 불가능 처리
        if current_jump_end <= i:
            print(-1)
            exit()

# 마지막 인덱스에 도달 가능한지 최종 확인
print(jumps if current_jump_end >= n - 1 else -1)