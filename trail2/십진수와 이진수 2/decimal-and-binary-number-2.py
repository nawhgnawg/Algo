N = input()

reversed_N = N[::-1]

demi = 0

for i, bit in enumerate(reversed_N):
    demi += int(bit) * (2 ** i)

demi *= 17

result = []

while demi > 0:
    result.append(demi % 2)
    demi = demi // 2

print("".join(map(str, result[::-1])))