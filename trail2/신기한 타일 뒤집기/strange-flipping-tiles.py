n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

# 딕셔너리를 사용하여 메모리 절약 및 시작점 오프셋 계산 생략
tiles = {}
current_x = 0

for x_str, d in commands:
    x = int(x_str)

    if d == 'L':
        # 현재 위치로부터 왼쪽으로 x칸 (현재 칸 포함)
        next_x = current_x - x + 1
        for i in range(next_x, current_x + 1):
            tiles[i] = 1
        current_x = next_x
    elif d == 'R':
        # 현재 위치부터 오른쪽으로 x칸 (현재 칸 포함)
        next_x = current_x + x - 1
        for i in range(current_x, next_x + 1):
            tiles[i] = 2
        current_x = next_x # 마지막으로 뒤집은 위치로 갱신

# 결과 카운트 (딕셔너리에 저장된 값들 중 1과 2의 개수를 셈)
white_count = list(tiles.values()).count(1)
black_count = list(tiles.values()).count(2)

print(f'{white_count} {black_count}')


# # 기본 0, 흰색 1, 검은색 2
# a = [0] * (2000 * 100)
# current_x = 100_000

# # 명령 실행
# for x, d in commands:
#     # 왼쪽일 때
#     if d == 'L':
#         next_x = current_x - int(x)
#         for i in range(next_x, current_x):
#             a[i] = 1
#         current_x = current_x - int(x)
#     # 오른쪽일 때
#     elif d == 'R':
#         next_x = current_x + int(x)
#         for i in range(current_x, next_x):
#             a[i] = 2
#         current_x = current_x + int(x)

# print(f'{a.count(1)} {a.count(2)}')
