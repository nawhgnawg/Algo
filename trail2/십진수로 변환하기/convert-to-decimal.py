binary = input()

answer = 0

l = len(binary)

i = 0
while l > 0:
    answer += int(binary[l - 1]) * (2 ** i)
    i += 1
    l -= 1

print(answer)