# 모험가 길드
N = 5                       # 모험가의 수
array = [2, 3, 1, 2, 2]     # 각 모험가의 공포도 값
result = 0                  # 모험가 그룹의 최대 수

array.sort()

count = 0                   # 현재 그룹에 포함된 모헙가 수
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)