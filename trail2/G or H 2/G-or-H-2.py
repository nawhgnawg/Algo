n = int(input())

people = []
for _ in range(n):
    pos, char = input().split()
    people.append((int(pos), char))

# 1. 사람들의 위치(좌표)를 기준으로 오름차순 정렬합니다.
people.sort(key=lambda x: x[0])

max_len = 0

# 2. 시작 사람(i)과 끝 사람(j)을 정하는 2중 for문
for i in range(n):
    g_cnt = 0
    h_cnt = 0
    for j in range(i, n):
        if people[j][1] == 'G':
            g_cnt += 1
        else:
            h_cnt += 1
        
        # 조건: G만 있거나, H만 있거나, 둘의 개수가 같은 경우
        if g_cnt == 0 or h_cnt == 0 or g_cnt == h_cnt:
            length = people[j][0] - people[i][0]
            max_len = max(max_len, length)

print(max_len)
