n = int(input())
s = input()

c_cnt = 0
co_cnt = 0
cow_cnt = 0

for char in s:
    if char == 'C':
        c_cnt += 1
    elif char == 'O':
        co_cnt += c_cnt
    elif char == 'W':
        cow_cnt += co_cnt

print(cow_cnt)

# answer = 0

# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
#                 answer += 1

# print(answer)