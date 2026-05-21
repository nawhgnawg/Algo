N, B = map(int, input().split())

result = []

while N > 0:
    result.append(N % B)
    N = N // B

for num in result[::-1]:
    print(num, end='')