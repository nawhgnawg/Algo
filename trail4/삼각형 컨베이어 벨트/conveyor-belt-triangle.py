n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = l + r + d

shift = t % (3 * n)

belt = belt[-shift:] + belt[:-shift]

print(*(belt[:n]))
print(*(belt[n:2 * n]))
print(*(belt[2 * n:]))
