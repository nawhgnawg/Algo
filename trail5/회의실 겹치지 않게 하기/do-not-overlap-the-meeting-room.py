n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 1. 끝나는 시간 기준 오름차순 정렬, 끝나는 시간이 같다면 시작 시간 기준 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = -1

# 2. 회의를 하나씩 확인하며 겹치지 않는 경우 선택
for s, e in meetings:
    # 이전 회의가 끝난 시간(또는 같거나 이후)에 시작할 수 있다면 회의 선택
    if s >= last_end_time:
        count += 1
        last_end_time = e

print(n - count)
