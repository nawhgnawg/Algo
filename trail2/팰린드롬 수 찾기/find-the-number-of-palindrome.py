x, y = map(int, input().split())

# x부터 y까지 순회하며 앞뒤가 같은 수(팰린드롬)를 카운트
answer = 0
for num in range(x, y + 1):
    s = str(num)
    if s == s[::-1]:
        answer += 1

print(answer)

