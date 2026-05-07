import sys

# 1. 입력 속도 개선 및 데이터 읽기
input = sys.stdin.read().split()
if not input:
    exit()

n = int(input[0])
points = []
for i in range(n):
    px = int(input[1 + i*2])
    py = int(input[2 + i*2])
    points.append((px, py))

# x좌표와 y좌표 분리
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# 2. 가능한 모든 직선 후보 (중복 제거)
candidates = []
for val in set(x_coords):
    candidates.append((0, val)) # x = val (세로선)
for val in set(y_coords):
    candidates.append((1, val)) # y = val (가로선)

num_c = len(candidates)
possible = False

# 3. 직선을 1개, 2개, 3개 고르는 경우를 모두 포함하는 로직
# 후보가 3개보다 적을 경우를 대비해 후보군을 보강합니다.
# (똑같은 직선을 여러 번 골라도 되도록 i, j, k 범위를 i, j부터 시작하게 함)
for i in range(num_c):
    for j in range(i, num_c):
        for k in range(j, num_c):
            # 선택된 3개의 직선 (i, j, k가 같으면 직선 1개나 2개만 쓰는 셈)
            l1 = candidates[i]
            l2 = candidates[j]
            l3 = candidates[k]

            all_covered = True
            for px, py in points:
                # 이 점이 세 직선 중 하나라도 지나는지 확인
                is_covered = False
                # 직선 1 확인
                if (l1[0] == 0 and px == l1[1]) or (l1[0] == 1 and py == l1[1]):
                    is_covered = True
                # 직선 2 확인
                if not is_covered and ((l2[0] == 0 and px == l2[1]) or (l2[0] == 1 and py == l2[1])):
                    is_covered = True
                # 직선 3 확인
                if not is_covered and ((l3[0] == 0 and px == l3[1]) or (l3[0] == 1 and py == l3[1])):
                    is_covered = True
                
                # 하나라도 못 덮으면 이 조합은 꽝!
                if not is_covered:
                    all_covered = False
                    break
            
            if all_covered:
                possible = True
                break
        if possible: break
    if possible: break

print(1 if possible else 0)