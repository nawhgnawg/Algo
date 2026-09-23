str = input()

counts = {}

for i, c in enumerate(str):
    if c not in counts:
        counts[c] = [i, 1]
    else:
        counts[c][1] += 1

ans = "None"
for c, (first_idx, cnt) in counts.items():
    if cnt == 1:
        ans = c
        break

print(ans)
