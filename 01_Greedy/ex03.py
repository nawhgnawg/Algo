# 숫자 카드 게임
N = 3   # 행의 개수
M = 3   # 열의 개수
arrays = [[3, 1, 3],
         [4, 1, 4],
         [2, 2, 2]]

min_array = []
for array in arrays:
    min_array.append(min(array))

print(max(min_array))