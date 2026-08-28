n, k = map(int, input().split())

MAX_X = 10000

answer = 0

points = [0] * (MAX_X + 1)

for _ in range(n):
    a, x = map(int, input().split())
    points[x] += a

max_candy = 0

for i in range(k, MAX_X - k + 1):
    curr_candy = sum(points[i - k: i + k + 1])
    max_candy = max(curr_candy, max_candy)


print(max_candy)

