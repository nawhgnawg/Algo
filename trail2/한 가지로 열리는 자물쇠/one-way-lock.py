n = int(input())
a, b, c = map(int, input().split())

answer = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            # 입력한 번호 (x, y, z)
            x, y, z = i + 1, j + 1, k + 1

            if abs(x - a) <= 2 or abs(y - b) <= 2 or abs(z - c) <= 2:
                answer += 1

print(answer)