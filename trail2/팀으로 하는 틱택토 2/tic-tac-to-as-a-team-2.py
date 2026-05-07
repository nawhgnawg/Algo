inp = [list(map(int, input())) for _ in range(3)]

# 모든 가능한 8개 줄을 리스트로 만듦.
lines = []

# 가로 3줄
for row in inp:
    lines.append(set(row))

# 세로 3줄
for j in range(3):
    lines.append({inp[0][j], inp[1][j], inp[2][j]})

# 대각선 2줄
lines.append({inp[0][0], inp[1][1], inp[2][2]})
lines.append({inp[0][2], inp[1][1], inp[2][0]})

# 팀 승리 카운트
winning_teams = set()

for line_set in lines:
    # 한줄에 정확히 2종류의 숫자만 있을 때만 팀 승리 가능성 있음
    if len(line_set) == 2:
        # 팀을 식별하기 위해 정렬된 튜플로 저장
        team = tuple(sorted(list(line_set)))
        winning_teams.add(team)

print(len(winning_teams))


         