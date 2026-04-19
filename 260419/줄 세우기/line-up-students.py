n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

students.sort(key=lambda x: (-x[0], -x[1], -x[2]))

for h, w, n in students:
    print(f'{h} {w} {n}')