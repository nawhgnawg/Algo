a, b = map(int, input().split())
n = input()

reversed_n = n[::-1]
a_result = 0
for i, bit in enumerate(reversed_n):
    a_result += int(bit) * (a ** i)

b_result = []

if a_result == 0:
    print(0)
else:

    while a_result > 0:
        b_result.append(a_result % b)
        a_result = a_result // b

print("".join(map(str, b_result[::-1])))
