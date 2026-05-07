n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# x, y 좌표의 최댓값을 구함 (루프 범위 설정용)
max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)

min_m = float('inf') # 최댓값 M의 최솟값을 저장할 변수

# x축과 y축에 평행한 직선은 항상 짝수에 그어짐
for x_line in range(0, max_x + 2, 2):
    for y_line in range(0, max_y + 2, 2):
        
        # 4개 구역의 점 개수 초기화 (좌하, 우하, 좌상, 우상)
        div = [0, 0, 0, 0]
        
        for x, y in points:
            if x < x_line and y < y_line:
                div[0] += 1
            elif x > x_line and y < y_line:
                div[1] += 1
            elif x < x_line and y > y_line:
                div[2] += 1
            elif x > x_line and y > y_line:
                div[3] += 1
        
        # 현재 직선(x_line, y_line)에서의 가장 많은 점의 개수 M
        current_max = max(div)
        
        # 전체 경우 중 M이 가장 작을 때를 찾음
        if current_max < min_m:
            min_m = current_max

print(min_m)

    