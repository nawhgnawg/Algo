n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

total = []
for i in range(n):
    sum = score1[i] + score2[i] + score3[i]
    total.append((name[i], sum))

total.sort(key=lambda x: x[1])
for n, sum in total:
    name_idx = name.index(n)
    print(f'{n} {score1[name_idx]} {score2[name_idx]} {score3[name_idx]}')
